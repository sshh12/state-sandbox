from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class UserBase(BaseModel):
    username: str


class UserResponse(UserBase):
    id: int
    username: str
    email: str
    credits: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class CreateUserRequest(BaseModel):
    username: str
    email: str


class AuthResponse(BaseModel):
    user: UserResponse
    token: str


class StateResponse(BaseModel):
    id: int
    name: str
    description: str
    turn_in_progress: bool
    flag_svg: str
    created_at: datetime
    updated_at: datetime
    user_id: int

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
    markdown_delta_report: Optional[str]
    json_state: dict
    state_id: int

    class Config:
        from_attributes = True


class CreateNewSnapshotRequest(BaseModel):
    policy: str


class AdviceRequest(BaseModel):
    question: str
    events: str


class AdviceResponse(BaseModel):
    markdown_advice: str


class BaseEvent(BaseModel):
    def json_line(self) -> str:
        """Convert event to a JSON line for streaming"""
        return self.model_dump_json() + "\n"


class StateCreatedEvent(BaseEvent):
    type: str = "state_created"
    id: int


class StateStatusEvent(BaseEvent):
    type: str = "status"
    message: str


class StateErrorEvent(BaseEvent):
    type: str = "error"
    message: str


class StateCompleteEvent(BaseEvent):
    type: str = "complete"
    state: StateResponse


class StateSnapshotCompleteEvent(BaseEvent):
    type: str = "state_snapshot_complete"
    state_snapshot: StateSnapshotResponse


class HeartbeatEvent(BaseEvent):
    type: str = "heartbeat"


class StateWithLatestSnapshotResponse(BaseModel):
    id: int
    name: str
    description: str
    flag_svg: str
    created_at: datetime
    updated_at: datetime
    latest_snapshot: StateSnapshotResponse
    cache_updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
