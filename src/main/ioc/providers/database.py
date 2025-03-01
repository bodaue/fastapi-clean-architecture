from collections.abc import AsyncIterable

from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from application.interfaces.transaction_manager import TransactionManager
from infrastructure.database.database import get_new_session_maker
from infrastructure.database.transaction_manager import TransactionManagerImpl
from main.config import PostgresConfig


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    def get_session_maker(
        self, config: PostgresConfig
    ) -> async_sessionmaker[AsyncSession]:
        return get_new_session_maker(config)

    @provide(scope=Scope.REQUEST)
    async def get_session(
        self, session_maker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with session_maker() as session:
            yield session

    transaction_manager = provide(
        TransactionManagerImpl, provides=TransactionManager, scope=Scope.REQUEST
    )
