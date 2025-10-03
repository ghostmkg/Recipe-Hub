from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import or_
from fastapi import HTTPException, status
from datetime import datetime
import logging

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserPasswordUpdate
from app.services.auth_service import AuthService

logger = logging.getLogger(__name__)


class UserService:
    """Service class for user-related operations"""

    @staticmethod
    def create_user(db: Session, user_create: UserCreate) -> User:
        """Create a new user"""
        # Check if username already exists
        if UserService.get_user_by_username(db, user_create.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already registered"
            )
        
        # Check if email already exists
        if UserService.get_user_by_email(db, user_create.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        # Hash password
        hashed_password = AuthService.get_password_hash(user_create.password)
        
        # Create user object
        user_data = user_create.dict(exclude={"password", "password_confirm"})
        user = User(**user_data, password_hash=hashed_password)
        
        try:
            db.add(user)
            db.commit()
            db.refresh(user)
            logger.info(f"User created successfully: {user.username}")
            return user
        except Exception as e:
            db.rollback()
            logger.error(f"Error creating user: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error creating user"
            )

    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
        """Get user by ID"""
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_user_by_username(db: Session, username: str) -> Optional[User]:
        """Get user by username"""
        return db.query(User).filter(User.username == username.lower()).first()

    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Optional[User]:
        """Get user by email"""
        return db.query(User).filter(User.email == email.lower()).first()

    @staticmethod
    def get_user_by_username_or_email(db: Session, username_or_email: str) -> Optional[User]:
        """Get user by username or email"""
        return db.query(User).filter(
            or_(
                User.username == username_or_email.lower(),
                User.email == username_or_email.lower()
            )
        ).first()

    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        """Get list of users with pagination"""
        return db.query(User).filter(User.is_active == True).offset(skip).limit(limit).all()

    @staticmethod
    def update_user(db: Session, user: User, user_update: UserUpdate) -> User:
        """Update user information"""
        update_data = user_update.dict(exclude_unset=True)
        
        for field, value in update_data.items():
            setattr(user, field, value)
        
        try:
            db.commit()
            db.refresh(user)
            logger.info(f"User updated successfully: {user.username}")
            return user
        except Exception as e:
            db.rollback()
            logger.error(f"Error updating user: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error updating user"
            )

    @staticmethod
    def update_password(db: Session, user: User, password_update: UserPasswordUpdate) -> User:
        """Update user password"""
        # Verify current password
        if not AuthService.verify_password(password_update.current_password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorrect current password"
            )
        
        # Hash new password
        new_password_hash = AuthService.get_password_hash(password_update.new_password)
        user.password_hash = new_password_hash
        
        try:
            db.commit()
            db.refresh(user)
            logger.info(f"Password updated successfully for user: {user.username}")
            return user
        except Exception as e:
            db.rollback()
            logger.error(f"Error updating password: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error updating password"
            )

    @staticmethod
    def deactivate_user(db: Session, user: User) -> User:
        """Deactivate user account"""
        user.is_active = False
        
        try:
            db.commit()
            db.refresh(user)
            logger.info(f"User deactivated: {user.username}")
            return user
        except Exception as e:
            db.rollback()
            logger.error(f"Error deactivating user: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error deactivating user"
            )

    @staticmethod
    def activate_user(db: Session, user: User) -> User:
        """Activate user account"""
        user.is_active = True
        
        try:
            db.commit()
            db.refresh(user)
            logger.info(f"User activated: {user.username}")
            return user
        except Exception as e:
            db.rollback()
            logger.error(f"Error activating user: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error activating user"
            )

    @staticmethod
    def verify_user(db: Session, user: User) -> User:
        """Verify user account"""
        user.is_verified = True
        
        try:
            db.commit()
            db.refresh(user)
            logger.info(f"User verified: {user.username}")
            return user
        except Exception as e:
            db.rollback()
            logger.error(f"Error verifying user: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error verifying user"
            )

    @staticmethod
    def update_last_login(db: Session, user: User) -> User:
        """Update user's last login timestamp"""
        user.last_login = datetime.utcnow()
        
        try:
            db.commit()
            db.refresh(user)
            return user
        except Exception as e:
            db.rollback()
            logger.error(f"Error updating last login: {str(e)}")
            return user  # Non-critical error, return user without update

    @staticmethod
    def delete_user(db: Session, user: User) -> bool:
        """Permanently delete user account"""
        try:
            db.delete(user)
            db.commit()
            logger.info(f"User deleted: {user.username}")
            return True
        except Exception as e:
            db.rollback()
            logger.error(f"Error deleting user: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error deleting user"
            )

    @staticmethod
    def search_users(db: Session, query: str, skip: int = 0, limit: int = 50) -> List[User]:
        """Search users by username, email, or name"""
        search_filter = or_(
            User.username.ilike(f"%{query}%"),
            User.email.ilike(f"%{query}%"),
            User.first_name.ilike(f"%{query}%"),
            User.last_name.ilike(f"%{query}%")
        )
        
        return db.query(User).filter(
            User.is_active == True,
            search_filter
        ).offset(skip).limit(limit).all()