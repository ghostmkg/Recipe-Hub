from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables
    """
    # Database
    DATABASE_URL: str = "sqlite:///./recipe_hub.db"
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173"]
    
    # File uploads
    UPLOAD_DIR: str = "uploads"
    MAX_FILE_SIZE: int = 5 * 1024 * 1024  # 5MB
    ALLOWED_EXTENSIONS: List[str] = [".jpg", ".jpeg", ".png", ".gif"]
    
    # Pagination
    DEFAULT_PAGE_SIZE: int = 20
    MAX_PAGE_SIZE: int = 100
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
