from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, UTC

from sqlalchemy.sql.operators import is_

from application.interfaces.session_repository import SessionRepository
from domain.entities.session import Session, SessionId
from domain.entities.user import UserId


class SQLSessionRepository(SessionRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, session: Session) -> Session:
        self._session.add(session)
        await self._session.flush()
        return session

    async def get_by_id(self, session_id: SessionId) -> Session | None:
        return await self._session.get(Session, session_id)

    async def get_active_by_user_id(self, user_id: UserId) -> list[Session]:
        stmt = select(Session).where(
            (Session.user_id == user_id),
            is_(Session.is_active, True),
            (Session.expires_at > datetime.now(UTC)),
        )
        result = await self._session.execute(stmt)
        return list(result.scalars())

    async def delete(self, session_id: SessionId) -> None:
        stmt = delete(Session).where(Session.id == session_id)
        await self._session.execute(stmt)
