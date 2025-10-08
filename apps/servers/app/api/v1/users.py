from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from app.core.database import SessionLocal
from app.core.security import verify_password, get_password_hash, create_access_token
from app.models import user as user_model
from app.schemas import user as user_schema
from app.deps.auth import get_current_user
from app.core.config import settings

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/register", response_model=user_schema.UserRead, status_code=status.HTTP_201_CREATED, summary="Register a new user")
def register_user(payload: user_schema.UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user account.
    """
    existing_user = db.query(user_model.User).filter(user_model.User.email == payload.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(payload.password)
    new_user = user_model.User(email=payload.email, name=payload.name, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/users/login", response_model=user_schema.Token, summary="Authenticate user and get access token")
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Authenticate a user using email and password, then return a JWT token.
    """
    user = db.query(user_model.User).filter(user_model.User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(subject=user.id, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me", response_model=user_schema.UserRead, summary="Get current user profile")
def read_users_me(current_user: user_model.User = Depends(get_current_user)):
    """
    Return profile information for the authenticated user.
    """
    return current_user
