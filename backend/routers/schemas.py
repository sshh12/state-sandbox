from pydantic import BaseModel
from datetime import datetime
from typing import Optional


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
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
