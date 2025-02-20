from typing import Protocol
from uuid import UUID


class IdGenerator(Protocol):
    def __call__(self) -> UUID:
        pass
