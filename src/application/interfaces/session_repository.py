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
    async def deactivate(self, session_id: SessionId) -> None:
        raise NotImplementedError

    @abstractmethod
    async def deactivate_all_for_user(self, user_id: UserId) -> None:
        raise NotImplementedError
