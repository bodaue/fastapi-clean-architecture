from abc import abstractmethod
from typing import Protocol

from domain.entities.session import Session, SessionId
from domain.entities.user import UserId


class SessionRepository(Protocol):
    @abstractmethod
    async def create(self, session: Session) -> Session:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, session_id: SessionId) -> Session | None:
        raise NotImplementedError

    @abstractmethod
    async def get_active_by_user_id(self, user_id: UserId) -> list[Session]:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, session_id: SessionId) -> None:
        raise NotImplementedError
