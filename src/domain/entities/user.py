from dataclasses import dataclass
from typing import NewType

from domain.exceptions import UserNotActiveError

UserId = NewType("UserId", int)


@dataclass
class User:
    id: UserId | None
    email: str
    hashed_password: str
    is_active: bool = True

    def ensure_is_active(self) -> None:
        if not self.is_active:
            raise UserNotActiveError
