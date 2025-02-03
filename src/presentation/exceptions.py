from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from starlette import status
from starlette.responses import Response

from application import exceptions as app_exc
from domain import exceptions as domain_exc
from infrastructure import exceptions as infra_exc


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(domain_exc.UserNotActiveError)
    async def user_not_active_handler(_: Request, __: Exception) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={"detail": "User does not exists"},
        )

    @app.exception_handler(app_exc.UserAlreadyExistsError)
    async def user_already_exists_handler(_: Request, exc: Exception) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": str(exc)},
        )

    @app.exception_handler(app_exc.InvalidCredentialsError)
    async def invalid_credentials_handler(_: Request, __: Exception) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": "Invalid credentials."},
        )

    @app.exception_handler(infra_exc.AuthenticationError)
    async def authentication_exception_handler(_: Request, __: Exception) -> Response:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": "Invalid username or password."},
        )
