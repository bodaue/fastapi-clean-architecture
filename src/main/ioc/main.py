from dishka import AsyncContainer, make_async_container

from main.config import Config
from main.ioc.providers.database import DatabaseProvider


def create_container(config: Config) -> AsyncContainer:
    return make_async_container(DatabaseProvider(), context={Config: config})
