from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from infrastructure.database.tables.map import map_tables
from main.config import create_config, Config
from main.ioc.main import create_container
from presentation.controllers import auth
from presentation.exceptions import register_exception_handlers
from presentation.middlewares.session import SessionMiddleware

from dishka import AsyncContainer


def setup_routers(app: FastAPI) -> None:
    app.include_router(auth.router)


def setup_middlewares(app: FastAPI, config: Config) -> None:
    app.add_middleware(
        BaseHTTPMiddleware, SessionMiddleware(session_config=config.session)
    )


def create_application() -> FastAPI:
    config: Config = create_config()
    app: FastAPI = FastAPI(title=config.app.title, debug=config.app.debug)

    container: AsyncContainer = create_container(config)
    setup_dishka(container, app)

    setup_routers(app)
    setup_middlewares(app, config)
    register_exception_handlers(app)

    map_tables()

    return app
