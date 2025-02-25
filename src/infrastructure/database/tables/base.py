from sqlalchemy import MetaData
from sqlalchemy.orm import registry

from infrastructure.database.tables.session import map_sessions_table
from infrastructure.database.tables.user import map_users_table

metadata: MetaData = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

mapper_registry: registry = registry(metadata=metadata)


def map_tables() -> None:
    map_users_table()
    map_sessions_table()
