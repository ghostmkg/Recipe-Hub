from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.user import UserCreate, UserUpdate, UserOut
from app.services.user_service import create_user, list_users, get_user
from app.core.database import get_db

router = APIRouter()

# Create a new user
@router.post("/", response_model=UserOut)
async def create_new_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await create_user(db, user)
    return db_user

# List all users
@router.get("/", response_model=List[UserOut])
async def get_all_users(db: AsyncSession = Depends(get_db)):
    users = await list_users(db)
    return users

# Get a user by ID
@router.get("/{user_id}", response_model=UserOut)
async def get_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update a user
@router.put("/{user_id}", response_model=UserOut)
async def update_user_info(user_id: int, user_update: UserUpdate, db: AsyncSession = Depends(get_db)):
    from app.services.user_service import update_user
    updated_user = await update_user(db, user_id, user_update)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user
