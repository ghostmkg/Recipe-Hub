import os
from pathlib import Path
from pydantic import BaseSettings, AnyHttpUrl
from typing import List

# Get project base directory (two levels up from this file)
BASE_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    PROJECT_NAME: str = "Recipes API"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "replace-me-in-prod")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    SQLALCHEMY_DATABASE_URI: str = f"sqlite:///{BASE_DIR.parent.parent / 'data' / 'app.db'}"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:5173",  # Vite default port
        "http://localhost:3000"   # Optional frontend port
    ]

    class Config:
        env_file = BASE_DIR.parent.parent / ".env"
        env_file_encoding = "utf-8"

settings = Settings()
