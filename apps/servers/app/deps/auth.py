from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import User
from app.services.auth_service import AuthService
from app.services.user_service import UserService

# HTTP Bearer token scheme
security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """
    Dependency to get the current authenticated user from JWT token
    """
    token = credentials.credentials
    
    try:
        # Decode token and get user
        payload = AuthService.decode_token(token)
        user_id: str = payload.get("sub")
        
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Get user from database
        user = UserService.get_user_by_id(db, user_id=int(user_id))
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Check if user is active
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Inactive user"
            )
        
        return user
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """
    Dependency to get the current active user
    """
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )
    return current_user


def get_current_verified_user(current_user: User = Depends(get_current_user)) -> User:
    """
    Dependency to get the current verified user
    """
    if not current_user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User not verified"
        )
    return current_user


def get_current_superuser(current_user: User = Depends(get_current_user)) -> User:
    """
    Dependency to get the current superuser
    """
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    return current_user


def get_optional_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    db: Session = Depends(get_db)
) -> Optional[User]:
    """
    Dependency to optionally get the current user (for endpoints that work with or without auth)
    """
    if not credentials:
        return None
    
    try:
        token = credentials.credentials
        payload = AuthService.decode_token(token)
        user_id: str = payload.get("sub")
        
        if user_id is None:
            return None
        
        user = UserService.get_user_by_id(db, user_id=int(user_id))
        if user is None or not user.is_active:
            return None
        
        return user
        
    except Exception:
        return None


# Alternative dependencies for different authentication requirements
def require_active_user(current_user: User = Depends(get_current_active_user)) -> User:
    """Require an active user"""
    return current_user


def require_verified_user(current_user: User = Depends(get_current_verified_user)) -> User:
    """Require a verified user"""
    return current_user


def require_superuser(current_user: User = Depends(get_current_superuser)) -> User:
    """Require a superuser"""
    return current_user