from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter

from application.interactors.login_user import (
    LoginUserInteractor,
    LoginUserRequest,
    LoginUserResponse,
)
from application.interactors.register_user import (
    RegisterUserInteractor,
    RegisterUserRequest,
    RegisterUserResponse,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register",
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
    responses={
        401: {"description": "Invalid username of password"},
        403: {"description": "User is not active"},
    },
)
@inject
async def login(
    data: LoginUserRequest, login_user: FromDishka[LoginUserInteractor]
) -> LoginUserResponse:
    return await login_user(data)
