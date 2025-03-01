from dataclasses import dataclass
from typing import NewType
from datetime import datetime

from domain.entities.user import UserId

SessionId = NewType("SessionId", str)


@dataclass
class Session:
    id: SessionId
    user_id: UserId
    expires_at: datetime
    created_at: datetime = None
    is_active: bool = True
