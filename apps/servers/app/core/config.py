from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Recipe Hub"
    VERSION: str = "1.0.0"
    DATABASE_URL: str = "sqlite:///./recipes.db"
    ALLOWED_ORIGINS: list[str] = ["*"]

    class Config:
        env_file = ".env"


settings = Settings()
