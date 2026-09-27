from pathlib import Path

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


BACKEND_ROOT = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    database_url: str
    media_storage_path: Path = Path("var/media")
    redis_url: str
    jwt_secret_key: str
    jwt_algorithm: str
    jwt_access_token_expire_minutes: int

    model_config = SettingsConfigDict(
        env_file=BACKEND_ROOT / ".env",
        env_file_encoding="utf-8",
    )

    @field_validator("media_storage_path")
    @classmethod
    def resolve_media_storage_path(cls, path: Path) -> Path:
        """Resolve relative upload paths against the backend directory."""
        return (BACKEND_ROOT / path).resolve()


settings = Settings()
