from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings as _BaseSettings
from pydantic_settings import SettingsConfigDict
from sqlalchemy import URL


class BaseSettings(_BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore", env_file=".env", env_file_encoding="utf-8"
    )


class ServerSettings(BaseSettings, env_prefix="SERVER_"):
    host: str
    port: int


class PostgresSettings(BaseSettings, env_prefix="POSTGRES_"):
    host: str
    port: int

    username: str
    password: SecretStr

    database: str

    def build_dsn(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.username,
            password=self.password.get_secret_value(),
            host=self.host,
            port=self.port,
            database=self.database,
        )


class Settings(BaseModel):
    server: ServerSettings
    postgres: PostgresSettings


def create_settings() -> Settings:
    return Settings(
        server=ServerSettings(),
        postgres=PostgresSettings(),
    )


settings = create_settings()
