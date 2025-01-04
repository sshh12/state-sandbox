from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Literal, Union


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
    markdown_events: Optional[str]
    json_state: dict
    state_id: int

    class Config:
        from_attributes = True


class CreateNewSnapshotRequest(BaseModel):
    policy: str


class AdviceRequest(BaseModel):
    question: str


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


class StateCompleteEvent(BaseEvent):
    type: str = "complete"
    state: StateResponse


StateCreationEvent = Union[StateCreatedEvent, StateStatusEvent, StateCompleteEvent]
