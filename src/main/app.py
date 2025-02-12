from typing import TYPE_CHECKING

from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from main.config import create_config, Config
from main.ioc.main import create_container
from presentation.controllers import auth
from presentation.exceptions import register_exception_handlers

if TYPE_CHECKING:
    from dishka import AsyncContainer


def setup_routers(app: FastAPI) -> None:
    app.include_router(auth.router)


def create_application() -> FastAPI:
    config: Config = create_config()
    app: FastAPI = FastAPI(title=config.app.title, debug=config.app.debug)

    container: AsyncContainer = create_container(config)
    setup_dishka(container, app)

    setup_routers(app)
    register_exception_handlers(app)

    return app
