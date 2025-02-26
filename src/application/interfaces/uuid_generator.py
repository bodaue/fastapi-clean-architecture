from typing import Protocol
from uuid import UUID


class UUIDGenerator(Protocol):
    def __call__(self) -> UUID: ...
