from abc import abstractmethod
from typing import Protocol

from domain.entities.user import UserId


class TokenProcessor(Protocol):
    @abstractmethod
    def create_access_token(self, user_id: UserId) -> str:
        raise NotImplementedError

    @abstractmethod
    def validate_token(self, token: str) -> UserId:
        raise NotImplementedError
