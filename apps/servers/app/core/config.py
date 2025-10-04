from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    ALLOWED_ORIGINS: List[str] = ["*"]  

settings = Settings()
