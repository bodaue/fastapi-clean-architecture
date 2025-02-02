from dishka import AsyncContainer, make_async_container

from main.config import Config
from main.ioc.providers.database import DatabaseProvider
from main.ioc.providers.interactor import InteractorProvider
from main.ioc.providers.repository import RepositoryProvider
from main.ioc.providers.service import ServiceProvider


def create_container(config: Config) -> AsyncContainer:
    return make_async_container(
        DatabaseProvider(),
        RepositoryProvider(),
        ServiceProvider(),
        InteractorProvider(),
        context={Config: config},
    )
