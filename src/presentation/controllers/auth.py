from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from starlette import status

from application.interactors.login_user import (
    LoginUserInteractor,
    LoginUserRequest,
)
from application.interactors.logout_user import LogoutUserInteractor
from application.interactors.register_user import (
    RegisterUserInteractor,
    RegisterUserRequest,
    RegisterUserResponse,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    responses={
        409: {"description": "User already exists"},
    },
)
@inject
async def register(
    data: RegisterUserRequest,
    register_user: FromDishka[RegisterUserInteractor],
) -> RegisterUserResponse:
    return await register_user(data)


@router.post(
    "/login",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        401: {"description": "Invalid username of password"},
        403: {"description": "User is not active"},
    },
)
@inject
async def login(
    data: LoginUserRequest, login_user: FromDishka[LoginUserInteractor]
) -> None:
    return await login_user(data)


@router.post(
    "/logout",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        401: {"description": "Authentication required"},
    },
)
@inject
async def logout(logout_user: FromDishka[LogoutUserInteractor]) -> None:
    return await logout_user()
