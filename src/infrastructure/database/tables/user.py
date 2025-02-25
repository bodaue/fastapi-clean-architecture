from sqlalchemy import String, Table, Column, Boolean, UUID

from domain.entities.user import User
from infrastructure.database.tables.base import metadata, mapper_registry

users_table = Table(
    "users",
    metadata,
    Column("id", UUID, primary_key=True),
    Column("email", String(256), unique=True, nullable=False),
    Column("hashed_password", String(1024), nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
)


def map_users_table() -> None:
    mapper_registry.map_imperatively(User, users_table)
