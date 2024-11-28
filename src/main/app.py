from fastapi import FastAPI


def setup_routers(app: FastAPI) -> None:
    pass


def setup_di_container(app: FastAPI) -> None:
    pass


def create_application() -> FastAPI:
    app = FastAPI(
        title="FastAPI Template",
        debug=True,
        root_path="/api/v1",
    )
    setup_di_container(app)
    setup_routers(app)
    return app
