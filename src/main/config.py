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


class JWTConfig(BaseSettings, env_prefix="JWT_"):
    secret_key: SecretStr
    algorithm: Literal["HS256", "HS384", "HS512", "RS256", "RS384", "RS512"]
    access_token_expires_minutes: int


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
    jwt: JWTConfig
    postgres: PostgresConfig
    redis: RedisConfig


def create_config() -> Config:
    return Config(
        app=ApplicationConfig(),
        jwt=JWTConfig(),
        postgres=PostgresConfig(),
        redis=RedisConfig(),
    )
