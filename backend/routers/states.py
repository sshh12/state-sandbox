from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from db.models import State
from routers.schemas import StateResponse
from routers.auth import get_current_user_from_token

router = APIRouter(prefix="/api/states", tags=["states"])


@router.get("", response_model=List[StateResponse])
async def get_states(
    current_user=Depends(get_current_user_from_token), db: Session = Depends(get_db)
):
    states = db.query(State).filter(State.user_id == current_user.id).all()
    return states
