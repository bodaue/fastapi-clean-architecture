from dishka import AsyncContainer, make_async_container

from main.config import Config


def create_container(config: Config) -> AsyncContainer:
    return make_async_container(context={Config: config})
