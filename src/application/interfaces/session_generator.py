from typing import Protocol

from domain.entities.session import SessionId


class SessionIdGenerator(Protocol):
    def __call__(self) -> SessionId: ...
