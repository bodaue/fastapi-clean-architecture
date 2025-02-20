from abc import abstractmethod
from typing import Protocol

from domain.entities.user import UserId


class IdentityProvider(Protocol):
    @abstractmethod
    async def get_current_user_id(self) -> UserId:
        pass

    @abstractmethod
    async def is_authenticated(self) -> bool:
        pass
