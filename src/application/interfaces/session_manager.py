from abc import abstractmethod
from typing import Protocol

from domain.entities.session import Session, SessionId
from domain.entities.user import UserId


class SessionManager(Protocol):
    @abstractmethod
    async def add(self, session: Session) -> None:
        pass

    @abstractmethod
    async def get_user_id(self, session_id: SessionId) -> UserId:
        pass

    @abstractmethod
    async def get_current_session_id(self) -> SessionId:
        pass
