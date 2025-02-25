from infrastructure.database.tables.session import map_sessions_table
from infrastructure.database.tables.user import map_users_table


def map_tables() -> None:
    map_users_table()
    map_sessions_table()
