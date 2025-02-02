from abc import abstractmethod
from typing import Protocol

from domain.entities.user import UserId


class IdProvider(Protocol):
    @abstractmethod
    def get_current_user_id(self) -> UserId:
        raise NotImplementedError
