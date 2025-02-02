# src/presentation/exception_handlers.py

from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from starlette.responses import Response

from domain.exceptions.access import AuthenticationError, UserAlreadyExistsError


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(AuthenticationError)
    async def authentication_exception_handler(
        _: Request, __: AuthenticationError
    ) -> Response:
        return JSONResponse(
            status_code=401,
            content={"detail": "Неверные учетные данные или токен."},
        )

    @app.exception_handler(UserAlreadyExistsError)
    async def user_already_exists_handler(
        _: Request, __: UserAlreadyExistsError
    ) -> Response:
        return JSONResponse(
            status_code=409,
            content={"detail": "Пользователь уже существует"},
        )
