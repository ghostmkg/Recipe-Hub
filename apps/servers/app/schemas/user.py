from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, validator
import re


class UserBase(BaseModel):
    """Base user schema with common fields"""
    username: str = Field(..., min_length=3, max_length=50, description="Unique username")
    email: EmailStr = Field(..., description="User email address")
    first_name: Optional[str] = Field(None, max_length=50, description="User's first name")
    last_name: Optional[str] = Field(None, max_length=50, description="User's last name")
    bio: Optional[str] = Field(None, max_length=500, description="User bio")
    avatar_url: Optional[str] = Field(None, description="URL to user's avatar image")

    @validator('username')
    def validate_username(cls, v):
        """Validate username format"""
        if not re.match(r'^[a-zA-Z0-9_]+$', v):
            raise ValueError('Username must contain only letters, numbers, and underscores')
        return v.lower()

    @validator('avatar_url')
    def validate_avatar_url(cls, v):
        """Validate avatar URL format"""
        if v and not v.startswith(('http://', 'https://')):
            raise ValueError('Avatar URL must be a valid HTTP/HTTPS URL')
        return v


class UserCreate(UserBase):
    """Schema for creating a new user"""
    password: str = Field(..., min_length=8, max_length=100, description="User password")
    password_confirm: str = Field(..., description="Password confirmation")

    @validator('password')
    def validate_password(cls, v):
        """Validate password strength"""
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'\d', v):
            raise ValueError('Password must contain at least one digit')
        return v

    @validator('password_confirm')
    def passwords_match(cls, v, values):
        """Validate that passwords match"""
        if 'password' in values and v != values['password']:
            raise ValueError('Passwords do not match')
        return v


class UserLogin(BaseModel):
    """Schema for user login"""
    username_or_email: str = Field(..., description="Username or email address")
    password: str = Field(..., description="User password")


class UserUpdate(BaseModel):
    """Schema for updating user information"""
    first_name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    bio: Optional[str] = Field(None, max_length=500)
    avatar_url: Optional[str] = None

    @validator('avatar_url')
    def validate_avatar_url(cls, v):
        """Validate avatar URL format"""
        if v and not v.startswith(('http://', 'https://')):
            raise ValueError('Avatar URL must be a valid HTTP/HTTPS URL')
        return v


class UserPasswordUpdate(BaseModel):
    """Schema for updating user password"""
    current_password: str = Field(..., description="Current password")
    new_password: str = Field(..., min_length=8, max_length=100, description="New password")
    new_password_confirm: str = Field(..., description="New password confirmation")

    @validator('new_password')
    def validate_new_password(cls, v):
        """Validate new password strength"""
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'\d', v):
            raise ValueError('Password must contain at least one digit')
        return v

    @validator('new_password_confirm')
    def passwords_match(cls, v, values):
        """Validate that new passwords match"""
        if 'new_password' in values and v != values['new_password']:
            raise ValueError('New passwords do not match')
        return v


class UserResponse(UserBase):
    """Schema for user response (public user data)"""
    id: int
    is_active: bool
    is_verified: bool
    joined_at: datetime
    last_login: Optional[datetime] = None
    full_name: Optional[str] = None

    class Config:
        from_attributes = True

    @validator('full_name', pre=True, always=True)
    def compute_full_name(cls, v, values):
        """Compute full name from first and last name"""
        if v:
            return v
        first_name = values.get('first_name')
        last_name = values.get('last_name')
        username = values.get('username')
        
        if first_name and last_name:
            return f"{first_name} {last_name}"
        elif first_name:
            return first_name
        elif last_name:
            return last_name
        return username


class UserProfile(UserResponse):
    """Extended user profile with additional information"""
    recipe_count: Optional[int] = 0
    total_ratings: Optional[int] = 0
    average_rating: Optional[float] = 0.0


class UserInDB(UserBase):
    """Schema for user in database (includes sensitive data)"""
    id: int
    password_hash: str
    is_active: bool
    is_verified: bool
    is_superuser: bool
    joined_at: datetime
    last_login: Optional[datetime] = None

    class Config:
        from_attributes = True


class Token(BaseModel):
    """Schema for authentication token"""
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    user: UserResponse


class TokenData(BaseModel):
    """Schema for token data"""
    user_id: Optional[int] = None
    username: Optional[str] = None