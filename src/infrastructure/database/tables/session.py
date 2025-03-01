from sqlalchemy import String, ForeignKey, DateTime, Table, Column, UUID, Boolean
from sqlalchemy.sql import func

from domain.entities.session import Session
from infrastructure.database.tables.base import metadata, mapper_registry

sessions_table = Table(
    "sessions",
    metadata,
    Column("id", String, primary_key=True),
    Column("user_id", UUID, ForeignKey("users.id"), nullable=False, unique=True),
    Column(
        "created_at",
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    ),
    Column("expires_at", DateTime(timezone=True), nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
)


def map_sessions_table() -> None:
    mapper_registry.map_imperatively(Session, sessions_table)
