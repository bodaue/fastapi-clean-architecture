from dishka import AsyncContainer, make_async_container
from dishka.integrations.fastapi import FastapiProvider

from main.config import Config
from main.ioc.providers.core import ConfigProvider
from main.ioc.providers.database import DatabaseProvider
from main.ioc.providers.interactor import InteractorProvider
from main.ioc.providers.repository import RepositoryProvider
from main.ioc.providers.service import ServiceProvider
from main.ioc.providers.adapter import AdapterProvider


def create_container(config: Config) -> AsyncContainer:
    return make_async_container(
        FastapiProvider(),
        ConfigProvider(),
        ServiceProvider(),
        DatabaseProvider(),
        RepositoryProvider(),
        AdapterProvider(),
        InteractorProvider(),
        context={Config: config},
    )
