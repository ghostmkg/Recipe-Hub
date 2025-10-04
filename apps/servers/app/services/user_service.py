from sqlalchemy.ext.asyncio import AsyncSession
"""
User service module for handling user-related database operations.
This module provides asynchronous functions to create, retrieve, list, and update user records
in the database using SQLAlchemy's AsyncSession. It also handles password hashing via the
AuthService.
Functions:
    create_user(db: AsyncSession, user: UserCreate)
        Create a new user with hashed password and store it in the database.
    get_user(db: AsyncSession, user_id: int)
        Retrieve a user by their unique ID.
    get_user_by_username(db: AsyncSession, username: str)
        Retrieve a user by their username.
    list_users(db: AsyncSession)
        Retrieve a list of all users.
    update_user(db: AsyncSession, user_id: int, user_update: UserUpdate)
        Update an existing user's information with provided fields.
"""
from sqlalchemy.future import select
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.services.auth_service import AuthService

async def create_user(db: AsyncSession, user: UserCreate):
    hashed_pw = AuthService.get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_pw)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()

async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(select(User).where(User.username == username))
    return result.scalar_one_or_none()

async def list_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()

async def update_user(db: AsyncSession, user_id: int, user_update: UserUpdate):
    user = await get_user(db, user_id)
    if not user:
        return None
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)
    await db.commit()
    await db.refresh(user)
    return user
