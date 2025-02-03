from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from pydantic import BaseModel, EmailStr, field_validator

from application.interactors.login_user import LoginUserInteractor
from application.interactors.register_user import RegisterUserInteractor

router = APIRouter(prefix="/auth", tags=["auth"])


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password", mode="before")
    @classmethod
    def validate_password(cls, value: str) -> str:
        min_length = 8
        if len(value) < min_length:
            raise ValueError("Password should contains at least 8 chars")
        if not any(char.isdigit() for char in value):
            raise ValueError("The password must contain at least 1 digit")
        return value


class LoginRequest(BaseModel):
    email: str
    password: str


class AuthResponse(BaseModel):
    token: str


@router.post(
    "/register",
    responses={
        409: {"description": "Пользователь с данным email уже существует."},
    },
)
@inject
async def register(
    request: RegisterRequest,
    register_user: FromDishka[RegisterUserInteractor],
) -> AuthResponse:
    token = await register_user(request.email, request.password)
    return AuthResponse(token=token)


@router.post(
    "/login",
    responses={
        401: {"description": "Неверные учётные данные или неактивный пользователь."}
    },
)
@inject
async def login(
    request: LoginRequest, login_user: FromDishka[LoginUserInteractor]
) -> AuthResponse:
    token = await login_user(request.email, request.password)
    return AuthResponse(token=token)
