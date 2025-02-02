from abc import abstractmethod
from typing import Protocol

from domain.entities.user import UserId, User


class UserRepository(Protocol):
    @abstractmethod
    async def create(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, user_id: UserId) -> User | None:
        raise NotImplementedError

    @abstractmethod
    async def get_by_email(self, email: str) -> User | None:
        raise NotImplementedError
