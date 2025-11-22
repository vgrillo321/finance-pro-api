# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./financiero.db"

    # TODO: Enable when moving to postgres
    # DATABASE_URL: str = "postgresql://postgres:secret@localhost:5432/financiero"

    class Config:
        env_file = ".env"

settings = Settings()
