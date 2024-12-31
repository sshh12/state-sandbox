from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class AuthResponse(BaseModel):
    user: UserResponse
    token: str
