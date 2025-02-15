from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func, and_
from typing import List, Optional
from datetime import datetime
from dateutil.relativedelta import relativedelta
import traceback
import asyncio
from fastapi_cache.decorator import cache

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
    StateErrorEvent,
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
    generate_state_description,
    generate_reasonable_policy_event,
)
from model.parsing import parse_state
from utils.event_stream import event_stream_response
from config import (
    CACHE_TTL_STATES_LEADERBOARD,
    CREDITS_NEW_STATE_COST,
    CREDITS_NEXT_YEAR_COST,
)

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
@cache(expire=CACHE_TTL_STATES_LEADERBOARD)
async def get_latest_state_snapshots(
    valueKeys: Optional[str] = None,
    db: Session = Depends(get_db),
):
    """Get the latest snapshot from all states along with state data. This endpoint is unauthenticated."""
    if valueKeys:
        valueKeys = valueKeys.split(",")

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
    current_time = datetime.now()
    for state, snapshot in latest_states:
        _fix_snapshot_json(snapshot, only_keys=valueKeys)
        result.append(
            StateWithLatestSnapshotResponse(
                id=state.id,
                name=state.name,
                description=state.description,
                flag_svg=state.flag_svg,
                created_at=state.created_at,
                updated_at=state.updated_at,
                latest_snapshot=snapshot,
                cache_updated_at=current_time,
            )
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
        if current_user.credits < CREDITS_NEW_STATE_COST:
            yield StateErrorEvent(
                message=f"Not enough credits ({current_user.credits} vs {CREDITS_NEW_STATE_COST}) to create a new state."
            ).json_line()
            return

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

        yield StateStatusEvent(
            message="Designing flag, events, and description..."
        ).json_line()
        svg_flag, random_events_md, state_description = await asyncio.gather(
            generate_state_flag(md_overview),
            generate_future_events(start_date, end_date, md_state, ""),
            generate_state_description(md_overview),
        )

        yield StateStatusEvent(message="Generating policy suggestions...").json_line()
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
        state.description = state_description
        db.add(state_snapshot)
        db.commit()
        db.refresh(state)

        yield StateCompleteEvent(state=state).json_line()

        current_user.credits -= CREDITS_NEW_STATE_COST
        db.add(current_user)
        db.commit()

    return event_stream_response(event_stream())


def _fix_snapshot_json(snapshot: StateSnapshot, only_keys: Optional[List[str]] = None):
    snapshot.json_state = parse_state(snapshot.markdown_state, only_keys=only_keys)
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
        if current_user.credits < CREDITS_NEXT_YEAR_COST:
            yield StateErrorEvent(
                message=f"Not enough credits ({current_user.credits} vs {CREDITS_NEXT_YEAR_COST}) to create a new state."
            ).json_line()
            return

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

        if state.turn_in_progress:
            yield StateErrorEvent(
                message="Turn already in progress, refresh and try again after a few minutes"
            ).json_line()
            return

        state.turn_in_progress = True
        db.add(state)
        db.commit()

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

        try:
            yield StateStatusEvent(message="Drafting your policies...").json_line()
            reasonable_policy = await generate_reasonable_policy_event(request.policy)

            yield StateStatusEvent(message="Simulating next year...").json_line()
            diff, next_state, simulated_events = await generate_next_state(
                start_date=current_date,
                end_date=next_date,
                prev_state=latest_snapshot.markdown_state,
                events=latest_snapshot.markdown_future_events,
                reasonable_policy=reasonable_policy,
                historical_events=historical_events,
            )

            yield StateStatusEvent(
                message="Generating report and events..."
            ).json_line()
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

            yield StateStatusEvent(
                message="Generating policy suggestions..."
            ).json_line()
            next_events_policy = await generate_future_policy_suggestion(
                start_date=next_date,
                end_date=next_date + relativedelta(months=12),
                prev_state=next_state,
                events=next_events,
            )

            current_user.credits -= CREDITS_NEXT_YEAR_COST
            db.add(current_user)
            db.commit()
        except Exception:
            print(traceback.format_exc())
            state.turn_in_progress = False
            db.add(state)
            db.commit()
            yield StateErrorEvent(
                message="Failed to simulate the changes. Try again. If issues persist, reduce policy actions."
            ).json_line()
            return

        # patch in the policy events selected by the user
        latest_snapshot.markdown_future_events = simulated_events
        state.turn_in_progress = False
        db.add(state)
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
