from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from datetime import timedelta

from app.core.database import get_db
from app.core.config import settings
from app.deps.auth import (
    get_current_user, 
    get_current_active_user, 
    require_superuser,
    get_optional_current_user
)
from app.models.user import User
from app.schemas.user import (
    UserCreate, 
    UserResponse, 
    UserUpdate, 
    UserLogin, 
    UserPasswordUpdate,
    UserProfile,
    Token
)
from app.services.user_service import UserService
from app.services.auth_service import AuthService

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(
    user_create: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Register a new user
    """
    return UserService.create_user(db, user_create)


@router.post("/login", response_model=Token)
def login_user(
    user_login: UserLogin,
    db: Session = Depends(get_db)
):
    """
    Login user and return access token
    """
    # Get user by username or email
    user = UserService.get_user_by_username_or_email(db, user_login.username_or_email)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username/email or password"
        )
    
    # Verify password
    if not AuthService.verify_password(user_login.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username/email or password"
        )
    
    # Check if user is active
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is inactive"
        )
    
    # Update last login
    UserService.update_last_login(db, user)
    
    # Create access token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = AuthService.create_access_token(
        data={"sub": str(user.id)},
        expires_delta=access_token_expires
    )
    
    return Token(
        access_token=access_token,
        token_type="bearer",
        expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        user=UserResponse.from_orm(user)
    )


@router.get("/me", response_model=UserProfile)
def get_current_user_profile(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Get current user's profile with extended information
    """
    # Get user statistics (recipe count, ratings, etc.)
    # This would be implemented when recipe and rating models are available
    profile_data = UserProfile.from_orm(current_user)
    profile_data.recipe_count = 0  # TODO: Count user's recipes
    profile_data.total_ratings = 0  # TODO: Count user's ratings
    profile_data.average_rating = 0.0  # TODO: Calculate average rating
    
    return profile_data


@router.put("/me", response_model=UserResponse)
def update_current_user(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Update current user's profile information
    """
    return UserService.update_user(db, current_user, user_update)


@router.put("/me/password", response_model=dict)
def update_current_user_password(
    password_update: UserPasswordUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Update current user's password
    """
    UserService.update_password(db, current_user, password_update)
    return {"message": "Password updated successfully"}


@router.delete("/me", response_model=dict)
def deactivate_current_user(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """
    Deactivate current user's account
    """
    UserService.deactivate_user(db, current_user)
    return {"message": "Account deactivated successfully"}


@router.get("/users", response_model=List[UserResponse])
def get_users(
    skip: int = Query(0, ge=0, description="Number of users to skip"),
    limit: int = Query(100, ge=1, le=100, description="Number of users to return"),
    search: Optional[str] = Query(None, description="Search users by username, email, or name"),
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_current_user)
):
    """
    Get list of users (public endpoint with optional authentication)
    """
    if search:
        users = UserService.search_users(db, search, skip, limit)
    else:
        users = UserService.get_users(db, skip, limit)
    
    return [UserResponse.from_orm(user) for user in users]


@router.get("/users/{user_id}", response_model=UserProfile)
def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_current_user)
):
    """
    Get user profile by ID (public endpoint)
    """
    user = UserService.get_user_by_id(db, user_id)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Get user statistics
    profile_data = UserProfile.from_orm(user)
    profile_data.recipe_count = 0  # TODO: Count user's recipes
    profile_data.total_ratings = 0  # TODO: Count user's ratings
    profile_data.average_rating = 0.0  # TODO: Calculate average rating
    
    return profile_data


@router.get("/users/username/{username}", response_model=UserProfile)
def get_user_by_username(
    username: str,
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_current_user)
):
    """
    Get user profile by username (public endpoint)
    """
    user = UserService.get_user_by_username(db, username)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Get user statistics
    profile_data = UserProfile.from_orm(user)
    profile_data.recipe_count = 0  # TODO: Count user's recipes
    profile_data.total_ratings = 0  # TODO: Count user's ratings
    profile_data.average_rating = 0.0  # TODO: Calculate average rating
    
    return profile_data


# Admin endpoints (require superuser permissions)
@router.put("/admin/users/{user_id}/activate", response_model=UserResponse)
def activate_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_superuser)
):
    """
    Activate a user account (admin only)
    """
    user = UserService.get_user_by_id(db, user_id)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return UserService.activate_user(db, user)


@router.put("/admin/users/{user_id}/deactivate", response_model=UserResponse)
def deactivate_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_superuser)
):
    """
    Deactivate a user account (admin only)
    """
    user = UserService.get_user_by_id(db, user_id)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return UserService.deactivate_user(db, user)


@router.put("/admin/users/{user_id}/verify", response_model=UserResponse)
def verify_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_superuser)
):
    """
    Verify a user account (admin only)
    """
    user = UserService.get_user_by_id(db, user_id)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return UserService.verify_user(db, user)


@router.delete("/admin/users/{user_id}", response_model=dict)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_superuser)
):
    """
    Permanently delete a user account (admin only)
    """
    user = UserService.get_user_by_id(db, user_id)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    UserService.delete_user(db, user)
    return {"message": f"User {user.username} deleted successfully"}
