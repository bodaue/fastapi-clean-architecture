from typing import Literal

from pydantic import SecretStr, BaseModel
from pydantic_settings import BaseSettings as _BaseSettings
from pydantic_settings import SettingsConfigDict
from sqlalchemy import URL


class BaseSettings(_BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore",
        env_file=".env",
        env_file_encoding="utf-8",
    )


class ApplicationConfig(BaseSettings, env_prefix="APPLICATION_"):
    title: str
    debug: bool = False


class SessionConfig(BaseSettings, env_prefix="SESSION_"):
    lifetime_minutes: int

    cookie_name: str = "session_id"
    samesite: Literal["lax", "strict", "none"] = "lax"
    path: str = "/"
    secure: bool = True
    domain: str | None = None


class PostgresConfig(BaseSettings, env_prefix="POSTGRES_"):
    host: str
    port: int
    user: str
    password: SecretStr
    db: str

    enable_logging: bool = False

    def build_dsn(self) -> str:
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.user,
            password=self.password.get_secret_value(),
            host=self.host,
            port=self.port,
            database=self.db,
        ).render_as_string(hide_password=False)


class RedisConfig(BaseSettings, env_prefix="REDIS_"):
    host: str
    port: int
    password: str


class Config(BaseModel):
    app: ApplicationConfig
    session: SessionConfig
    postgres: PostgresConfig
    redis: RedisConfig


def create_config() -> Config:
    return Config(
        app=ApplicationConfig(),
        session=SessionConfig(),
        postgres=PostgresConfig(),
        redis=RedisConfig(),
    )
