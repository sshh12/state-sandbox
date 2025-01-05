from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from dateutil.relativedelta import relativedelta

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
)
from routers.auth import get_current_user_from_token
from model.actions import (
    generate_state,
    generate_next_state,
    generate_state_flag,
    generate_diff_report,
    generate_state_advice,
)
from model.parsing import parse_state
from utils.event_stream import with_heartbeat, event_stream_response, HeartbeatResult

router = APIRouter(prefix="/api/states", tags=["states"])

START_DATE = "2000-01"


@router.get("", response_model=List[StateResponse])
async def get_states(
    current_user: User = Depends(get_current_user_from_token),
    db: Session = Depends(get_db),
):
    states = db.query(State).filter(State.user_id == current_user.id).all()
    return states


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
        state = State(
            date=date,
            name="Developing Nation",
            flag_svg='<svg xmlns="http://www.w3.org/2000/svg" width="900" height="600"></svg>',
            user_id=current_user.id,
        )
        db.add(state)
        db.flush()

        yield StateCreatedEvent(id=state.id).json_line()
        questions = [(q.question, q.value) for q in request.questions]

        yield StateStatusEvent(message="Generating initial state...").json_line()
        async for event in with_heartbeat(
            lambda: generate_state(date=date, name=request.name, questions=questions)
        ):
            if isinstance(event, HeartbeatResult):
                yield event.event
            else:
                md_state = event

        yield StateStatusEvent(message="Designing flag...").json_line()
        async for event in with_heartbeat(lambda: generate_state_flag(md_state)):
            if isinstance(event, HeartbeatResult):
                yield event.event
            else:
                svg_flag = event

        state_snapshot = StateSnapshot(
            date=date,
            state_id=state.id,
            markdown_state=md_state,
        )
        parsed_state = parse_state(state_snapshot.markdown_state)
        full_name = parsed_state["state_overview"]["basic_information"]["country_name"][
            "value"
        ]
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
    if snapshot.markdown_events:
        snapshot.json_state["events"] = snapshot.markdown_events.split("\n")
    else:
        snapshot.json_state["events"] = []
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
            .order_by(StateSnapshot.date.asc())
            .all()
        )
        if not previous_snapshots:
            raise HTTPException(status_code=404, detail="No previous snapshots found")

        latest_snapshot = previous_snapshots[-1]
        current_date = datetime.strptime(latest_snapshot.date, "%Y-%m")
        next_date = current_date + relativedelta(months=12)

        # Collect historical events with their dates
        historical_events = [
            (
                snapshot.date,
                (snapshot.markdown_events.split("\n")),
            )
            for snapshot in previous_snapshots
            if snapshot.markdown_events
        ]

        yield StateStatusEvent(message="Simulating next year...").json_line()
        async for event in with_heartbeat(
            lambda: generate_next_state(
                start_date=current_date,
                end_date=next_date,
                prev_state=latest_snapshot.markdown_state,
                policy=request.policy,
                historical_events=historical_events,
            )
        ):
            if isinstance(event, HeartbeatResult):
                yield event.event
            else:
                diff, next_state, next_events = event

        yield StateStatusEvent(message="Generating summary report...").json_line()
        async for event in with_heartbeat(
            lambda: generate_diff_report(
                start_date=current_date,
                end_date=next_date,
                prev_state=latest_snapshot.markdown_state,
                diff_output=diff,
            )
        ):
            if isinstance(event, HeartbeatResult):
                yield event.event
            else:
                next_state_report = event

        state_snapshot = StateSnapshot(
            date=next_date.strftime("%Y-%m"),
            state_id=state_id,
            markdown_state=next_state,
            markdown_delta=diff,
            markdown_delta_report=next_state_report,
            markdown_events=next_events,
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
        latest_snapshot.markdown_state, request.question
    )
    return AdviceResponse(markdown_advice=advice)
