from pydantic import BaseModel, EmailStr
from typing import Optional

# Shared properties
class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None


# Schema for user creation (registration)
class UserCreate(UserBase):
    password: str


# Schema for reading user data (response)
class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True


# Schema for JWT token response
class Token(BaseModel):
    access_token: str
    token_type: str
