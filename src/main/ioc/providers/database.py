from collections.abc import AsyncIterable

from dishka import Provider, provide, Scope, from_context
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from application.interfaces.committer import Committer
from infrastructure.database.committer import SQLAlchemyCommitter
from infrastructure.database.database import get_new_session_maker
from main.config import Config


class DatabaseProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def get_session_maker(self, config: Config) -> async_sessionmaker[AsyncSession]:
        return get_new_session_maker(config.postgres)

    @provide(scope=Scope.REQUEST)
    async def get_session(
        self, session_maker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with session_maker() as session:
            yield session

    committer = provide(SQLAlchemyCommitter, provides=Committer, scope=Scope.REQUEST)
