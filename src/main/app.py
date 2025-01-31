from collections.abc import Iterable

from dishka import make_async_container, Provider, AsyncContainer
from fastapi import FastAPI

from main.settings import create_settings, Settings


def create_application() -> FastAPI:
    return FastAPI(title="FastAPI Template", debug=True, root_path="/api/v1")


def create_di_container(providers: Iterable[Provider]) -> AsyncContainer:
    settings = create_settings()
    return make_async_container(*providers, context={Settings: settings})


def configure_application(app: FastAPI) -> None:
    pass
