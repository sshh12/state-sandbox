from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel

from db.database import get_db
from db.models import State, User
from routers.schemas import StateResponse, CreateStateRequest
from routers.auth import get_current_user_from_token

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
    print(f"Name: {request.name}")
    print("Questions:")
    for q in request.questions:
        print(f"- {q.question}: {q.value}")

    state = State(
        name="My Country",
        user_id=current_user.id,
    )
    db.add(state)
    db.commit()
    db.refresh(state)

    return state
