from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import State, StateSnapshot, User
from routers.schemas import StateResponse, CreateStateRequest, StateSnapshotResponse
from routers.auth import get_current_user_from_token
from model.actions import generate_state
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
    state = State(
        name=request.name,
        user_id=current_user.id,
    )
    db.add(state)
    db.flush()

    date = "2022-01"
    questions = [(q.question, q.value) for q in request.questions]
    state_snapshot = StateSnapshot(
        date=date,
        state_id=state.id,
        markdown_state=await generate_state(
            date=date, name=request.name, questions=questions
        ),
    )
    parsed_state = parse_state(state_snapshot.markdown_state)
    full_name = parsed_state["1. State Overview"]["Basic Information"]["Country Name"]
    state.name = full_name
    db.add(state_snapshot)
    db.commit()
    db.refresh(state)

    return state


@router.get("/{state_id}/snapshots", response_model=List[StateSnapshotResponse])
async def get_state_snapshots(
    state_id: int,
    db: Session = Depends(get_db),
):
    snapshots = db.query(StateSnapshot).filter(StateSnapshot.state_id == state_id).all()
    for snapshot in snapshots:
        snapshot.json_state = parse_state(snapshot.markdown_state)
        snapshot.json_state["date"] = snapshot.date
    return snapshots
