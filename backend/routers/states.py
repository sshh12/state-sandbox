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
)
from routers.auth import get_current_user_from_token
from model.actions import generate_state, generate_next_state, generate_state_flag
from model.parsing import parse_state

router = APIRouter(prefix="/api/states", tags=["states"])


@router.get("", response_model=List[StateResponse])
async def get_states(
    current_user: User = Depends(get_current_user_from_token),
    db: Session = Depends(get_db),
):
    states = db.query(State).filter(State.user_id == current_user.id).all()
    return states


@router.post("", response_model=StateResponse)
async def create_state(
    request: CreateStateRequest,
    current_user: User = Depends(get_current_user_from_token),
    db: Session = Depends(get_db),
):
    date = "2022-01"
    state = State(
        date=date,
        name="Developing Nation",
        flag_svg='<svg xmlns="http://www.w3.org/2000/svg" width="900" height="600"></svg>',
        user_id=current_user.id,
    )
    db.add(state)
    db.flush()

    questions = [(q.question, q.value) for q in request.questions]

    md_state = await generate_state(date=date, name=request.name, questions=questions)
    svg_flag = await generate_state_flag(md_state)
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

    return state


def _fix_snapshot_json(snapshot: StateSnapshot):
    snapshot.json_state = parse_state(snapshot.markdown_state)
    snapshot.json_state["date"] = snapshot.date
    snapshot.json_state["id"] = snapshot.id
    return snapshot


@router.get("/{state_id}/snapshots", response_model=List[StateSnapshotResponse])
async def get_state_snapshots(
    state_id: int,
    db: Session = Depends(get_db),
):
    snapshots = db.query(StateSnapshot).filter(StateSnapshot.state_id == state_id).all()
    for snapshot in snapshots:
        _fix_snapshot_json(snapshot)
    return snapshots


@router.post("/{state_id}/snapshots", response_model=StateSnapshotResponse)
async def create_state_snapshot(
    state_id: int,
    request: CreateNewSnapshotRequest,
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
    current_date = datetime.strptime(latest_snapshot.date, "%Y-%m")
    next_date = current_date + relativedelta(months=1)

    next_state, next_state_report = await generate_next_state(
        start_date=current_date,
        end_date=next_date,
        prev_state=latest_snapshot.markdown_state,
        policy=request.policy,
    )
    state_snapshot = StateSnapshot(
        date=next_date.strftime("%Y-%m"),
        state_id=state_id,
        markdown_state=next_state,
        markdown_delta_report=next_state_report,
    )
    db.add(state_snapshot)
    db.commit()
    db.refresh(state_snapshot)

    _fix_snapshot_json(state_snapshot)

    return state_snapshot
