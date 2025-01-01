from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class UserBase(BaseModel):
    username: str


class UserResponse(UserBase):
    id: int
    username: str
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class AuthResponse(BaseModel):
    user: UserResponse
    token: str


class StateResponse(BaseModel):
    id: int
    name: str
    flag_svg: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class QuestionInput(BaseModel):
    question: str
    value: int


class CreateStateRequest(BaseModel):
    name: str
    questions: List[QuestionInput]


class StateSnapshotResponse(BaseModel):
    id: int
    date: str
    markdown_state: str
    markdown_random_events: Optional[str]
    markdown_delta: Optional[str]
    markdown_delta_report: Optional[str]
    json_state: dict
    state_id: int

    class Config:
        from_attributes = True


class CreateNewSnapshotRequest(BaseModel):
    policy: str
