from pydantic import BaseModel, EmailStr
from typing import Optional

# Base class for shared attributes
class UserBase(BaseModel):
    username: str
    email: EmailStr

# Schema for creating a new user
class UserCreate(UserBase):
    password: str

# Schema for updating a user
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

# Schema for responses
class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True  # Allow reading SQLAlchemy models
