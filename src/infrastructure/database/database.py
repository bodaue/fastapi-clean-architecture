from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from main.config import PostgresConfig


def get_new_session_maker(
    postgres_config: PostgresConfig,
) -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(postgres_config.build_dsn())
    return async_sessionmaker(engine, autoflush=False, expire_on_commit=False)
