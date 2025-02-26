from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, UTC

from sqlalchemy.sql.operators import is_

from application.interfaces.session_repository import SessionRepository
from domain.entities.session import Session, SessionId
from domain.entities.user import UserId


class SQLSessionRepository(SessionRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, session: Session) -> Session:
        self.session.add(session)
        await self.session.flush()
        return session

    async def get_by_id(self, session_id: SessionId) -> Session | None:
        return await self.session.get(Session, session_id)

    async def get_active_by_user_id(self, user_id: UserId) -> list[Session]:
        stmt = select(Session).where(
            (Session.user_id == user_id),
            is_(Session.is_active, True),
            (Session.expires_at > datetime.now(UTC)),
        )
        result = await self.session.execute(stmt)
        return list(result.scalars())

    async def deactivate(self, session_id: SessionId) -> None:
        stmt = update(Session).where(Session.id == session_id).values(is_active=False)
        await self.session.execute(stmt)

    async def deactivate_all_for_user(self, user_id: UserId) -> None:
        stmt = (
            update(Session)
            .where((Session.user_id == user_id), is_(Session.is_active, True))
            .values(is_active=False)
        )
        await self.session.execute(stmt)
