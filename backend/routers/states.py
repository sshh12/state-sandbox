from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func, and_
from typing import List
from datetime import datetime
from dateutil.relativedelta import relativedelta
import asyncio

from db.database import get_db
from db.models import State, StateSnapshot, User
from routers.schemas import (
    StateResponse,
    CreateStateRequest,
    StateSnapshotResponse,
    CreateNewSnapshotRequest,
    AdviceRequest,
    AdviceResponse,
    StateCreatedEvent,
    StateStatusEvent,
    StateCompleteEvent,
    StateSnapshotCompleteEvent,
    StateWithLatestSnapshotResponse,
)
from routers.auth import get_current_user_from_token
from model.actions import (
    generate_state,
    generate_next_state,
    generate_state_flag,
    generate_diff_report,
    generate_state_advice,
    generate_future_events,
    generate_future_policy_suggestion,
)
from model.parsing import parse_state
from utils.event_stream import event_stream_response

router = APIRouter(prefix="/api/states", tags=["states"])

START_DATE = "2022-01"


@router.get("", response_model=List[StateResponse])
async def get_states(
    current_user: User = Depends(get_current_user_from_token),
    db: Session = Depends(get_db),
):
    states = db.query(State).filter(State.user_id == current_user.id).all()
    return states


@router.get("/latest", response_model=List[StateWithLatestSnapshotResponse])
async def get_latest_state_snapshots(
    db: Session = Depends(get_db),
):
    """Get the latest snapshot from all states along with state data. This endpoint is unauthenticated."""
    # Subquery to get the latest snapshot date for each state
    latest_dates = (
        db.query(StateSnapshot.state_id, func.max(StateSnapshot.date).label("max_date"))
        .group_by(StateSnapshot.state_id)
        .subquery()
    )

    # Query to get the states and their latest snapshots
    latest_states = (
        db.query(State, StateSnapshot)
        .join(StateSnapshot, State.id == StateSnapshot.state_id)
        .join(
            latest_dates,
            and_(
                StateSnapshot.state_id == latest_dates.c.state_id,
                StateSnapshot.date == latest_dates.c.max_date,
            ),
        )
        .all()
    )

    result = []
    for state, snapshot in latest_states:
        _fix_snapshot_json(snapshot)
        result.append(
            {
                "id": state.id,
                "name": state.name,
                "description": state.description,
                "flag_svg": state.flag_svg,
                "created_at": state.created_at,
                "updated_at": state.updated_at,
                "latest_snapshot": snapshot,
            }
        )

    return result


@router.get("/{state_id}", response_model=StateResponse)
async def get_state(
    state_id: int,
    db: Session = Depends(get_db),
):
    state = db.query(State).filter(State.id == state_id).first()
    if not state:
        raise HTTPException(status_code=404, detail="State not found")
    return state


@router.post("", response_model=None)
async def create_state(
    request: CreateStateRequest,
    current_user: User = Depends(get_current_user_from_token),
    db: Session = Depends(get_db),
):
    async def event_stream():
        date = START_DATE
        start_date = datetime.strptime(date, "%Y-%m")
        end_date = start_date + relativedelta(months=12)
        state = State(
            date=date,
            name="Developing Nation",
            description="A developing nation.",
            flag_svg='<svg xmlns="http://www.w3.org/2000/svg" width="900" height="600"></svg>',
            user_id=current_user.id,
        )
        db.add(state)
        db.flush()

        yield StateCreatedEvent(id=state.id).json_line()
        questions = [(q.question, q.value) for q in request.questions]

        yield StateStatusEvent(message="Generating initial state...").json_line()
        md_overview, md_state = await generate_state(
            date=date, name=request.name, questions=questions
        )

        yield StateStatusEvent(message="Designing flag...").json_line()
        svg_flag, random_events_md = await asyncio.gather(
            generate_state_flag(md_overview),
            generate_future_events(start_date, end_date, md_state, ""),
        )

        yield StateStatusEvent(message="Generating policy suggestion...").json_line()
        policy_suggestion = await generate_future_policy_suggestion(
            start_date, end_date, md_state, random_events_md
        )

        state_snapshot = StateSnapshot(
            date=date,
            state_id=state.id,
            markdown_state=md_state,
            markdown_future_events=random_events_md,
            markdown_future_events_policy=policy_suggestion,
        )
        parsed_state = parse_state(state_snapshot.markdown_state)
        full_name = parsed_state["government"]["government_metadata"][
            "country_official_name"
        ]["value"]
        state.name = full_name
        state.flag_svg = svg_flag
        db.add(state_snapshot)
        db.commit()
        db.refresh(state)

        yield StateCompleteEvent(state=state).json_line()

    return event_stream_response(event_stream())


def _fix_snapshot_json(snapshot: StateSnapshot):
    snapshot.json_state = parse_state(snapshot.markdown_state)
    snapshot.json_state["date"] = snapshot.date
    if snapshot.markdown_future_events:
        snapshot.json_state["events"] = snapshot.markdown_future_events.split("\n")
    else:
        snapshot.json_state["events"] = []
    if snapshot.markdown_future_events_policy:
        snapshot.json_state["events_policy"] = (
            snapshot.markdown_future_events_policy.split("\n")
        )
    else:
        snapshot.json_state["events_policy"] = ""
    if snapshot.markdown_delta_report:
        snapshot.json_state["delta_report"] = snapshot.markdown_delta_report
    else:
        snapshot.json_state["delta_report"] = ""
    snapshot.json_state["id"] = snapshot.id
    return snapshot


@router.get("/{state_id}/snapshots", response_model=List[StateSnapshotResponse])
async def get_state_snapshots(
    state_id: int,
    db: Session = Depends(get_db),
):
    snapshots = (
        db.query(StateSnapshot)
        .filter(StateSnapshot.state_id == state_id)
        .order_by(StateSnapshot.date.desc())
        .all()
    )
    for snapshot in snapshots:
        _fix_snapshot_json(snapshot)
    return snapshots


@router.post("/{state_id}/snapshots", response_model=None)
async def create_state_snapshot(
    state_id: int,
    request: CreateNewSnapshotRequest,
    current_user: User = Depends(get_current_user_from_token),
    db: Session = Depends(get_db),
):
    async def event_stream():
        state = (
            db.query(State)
            .filter(State.id == state_id, State.user_id == current_user.id)
            .first()
        )
        if not state:
            raise HTTPException(status_code=404, detail="State not found")

        # Get all previous snapshots ordered by date
        previous_snapshots = (
            db.query(StateSnapshot)
            .filter(StateSnapshot.state_id == state_id)
            .order_by(StateSnapshot.date.desc())
            .limit(10)
            .all()
        )[::-1]
        if not previous_snapshots:
            raise HTTPException(status_code=404, detail="No previous snapshots found")

        latest_snapshot = previous_snapshots[-1]
        current_date = datetime.strptime(latest_snapshot.date, "%Y-%m")
        next_date = current_date + relativedelta(months=12)

        # Collect historical events with their dates
        historical_events = [
            (
                snapshot.date,
                (snapshot.markdown_future_events.split("\n")),
            )
            for snapshot in previous_snapshots
            if snapshot.markdown_future_events
        ]

        yield StateStatusEvent(message="Simulating next year...").json_line()
        diff, next_state, simulated_events = await generate_next_state(
            start_date=current_date,
            end_date=next_date,
            prev_state=latest_snapshot.markdown_state,
            events=latest_snapshot.markdown_future_events,
            policy_input=request.policy,
            historical_events=historical_events,
        )

        yield StateStatusEvent(message="Generating summary report...").json_line()
        next_state_report, next_events = await asyncio.gather(
            generate_diff_report(
                start_date=current_date,
                end_date=next_date,
                prev_state=latest_snapshot.markdown_state,
                diff_output=diff,
            ),
            generate_future_events(
                start_date=next_date,
                end_date=next_date + relativedelta(months=12),
                prev_state=next_state,
                historical_events=historical_events,
            ),
        )

        yield StateStatusEvent(message="Generating policy suggestions...").json_line()
        next_events_policy = await generate_future_policy_suggestion(
            start_date=next_date,
            end_date=next_date + relativedelta(months=12),
            prev_state=next_state,
            events=next_events,
        )

        # patch in the policy events selected by the user
        latest_snapshot.markdown_future_events = simulated_events
        db.add(latest_snapshot)
        state_snapshot = StateSnapshot(
            date=next_date.strftime("%Y-%m"),
            state_id=state_id,
            markdown_state=next_state,
            markdown_delta=diff,
            markdown_delta_report=next_state_report,
            markdown_future_events=next_events,
            markdown_future_events_policy=next_events_policy,
        )
        db.add(state_snapshot)
        db.commit()
        db.refresh(state_snapshot)

        _fix_snapshot_json(state_snapshot)
        yield StateSnapshotCompleteEvent(state_snapshot=state_snapshot).json_line()

    return event_stream_response(event_stream())


@router.post("/{state_id}/advice", response_model=AdviceResponse)
async def get_advice(
    state_id: int,
    request: AdviceRequest,
    current_user: User = Depends(get_current_user_from_token),
    db: Session = Depends(get_db),
):
    state = (
        db.query(State)
        .filter(State.id == state_id, State.user_id == current_user.id)
        .first()
    )
    if not state:
        raise HTTPException(status_code=404, detail="State not found")

    latest_snapshot = (
        db.query(StateSnapshot)
        .filter(StateSnapshot.state_id == state_id)
        .order_by(StateSnapshot.date.desc())
        .first()
    )
    if not latest_snapshot:
        raise HTTPException(status_code=404, detail="State not found")
    advice = await generate_state_advice(
        latest_snapshot.markdown_state, request.question, request.events
    )
    return AdviceResponse(markdown_advice=advice)
