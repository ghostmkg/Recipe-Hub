from sqlalchemy import Column, String, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import BaseModel


class User(BaseModel):
    """
    User model for authentication and profile management
    """
    __tablename__ = "users"

    # Basic user information
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    
    # Profile information
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    bio = Column(Text, nullable=True)
    avatar_url = Column(String(500), nullable=True)
    
    # Account status
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    
    # Timestamps
    last_login = Column(DateTime(timezone=True), nullable=True)
    joined_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    recipes = relationship("Recipe", back_populates="author", cascade="all, delete-orphan")
    ratings = relationship("Rating", back_populates="user", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"
    
    @property
    def full_name(self):
        """Return the user's full name"""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        return self.username
