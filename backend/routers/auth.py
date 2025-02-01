from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import jwt, JWTError

from utils.emails import send_login_link
from db.database import get_db
from db.models import User
from routers.schemas import UserResponse, AuthResponse, CreateUserRequest
from config import JWT_SECRET_KEY, JWT_EXPIRATION_DAYS

router = APIRouter(prefix="/api/auth", tags=["auth"])

API_KEY_HEADER = APIKeyHeader(name="Authorization")


async def get_current_user_from_token(
    token: str = Security(API_KEY_HEADER), db: Session = Depends(get_db)
):
    try:
        token = token.replace("Bearer ", "")
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user


@router.post("/create", response_model=AuthResponse)
async def create_user(request: CreateUserRequest, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == request.email).first()
    if existing_user:
        if existing_user.email.endswith("sshh.io"):
            raise HTTPException(
                status_code=409,
                detail="Logging into temporary accounts is not supported.",
            )
        else:
            send_login_link(existing_user.email)
            raise HTTPException(
                status_code=409,
                detail="Account already exists. Check your email for a login link.",
            )

    try:
        new_user = User(username=request.username, email=request.email)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        token = jwt.encode(
            {
                "sub": new_user.username,
                "exp": datetime.now() + timedelta(days=JWT_EXPIRATION_DAYS),
            },
            JWT_SECRET_KEY,
            algorithm="HS256",
        )
        return AuthResponse(user=new_user, token=token)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/me", response_model=UserResponse)
async def get_current_user(current_user: User = Depends(get_current_user_from_token)):
    return current_user


@router.get("/email-login/{token}", response_model=AuthResponse)
async def email_login(token: str, db: Session = Depends(get_db)):
    try:
        # Decode the token
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
        email = payload.get("email")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        # Get the user
        user = db.query(User).filter(User.email == email).first()
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")

        # Generate a new session token
        session_token = jwt.encode(
            {
                "sub": user.username,
                "exp": datetime.now() + timedelta(days=JWT_EXPIRATION_DAYS),
            },
            JWT_SECRET_KEY,
            algorithm="HS256",
        )

        return AuthResponse(user=user, token=session_token)

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
