from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from pydantic import BaseModel

from application.interactors.login_user import LoginUserInteractor
from application.interactors.register_user import RegisterUserInteractor

router = APIRouter(prefix="/auth", tags=["auth"])


class RegisterRequest(BaseModel):
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


class AuthResponse(BaseModel):
    token: str


@router.post("/register")
@inject
async def register(
    request: RegisterRequest,
    register_user: FromDishka[RegisterUserInteractor],
) -> AuthResponse:
    token = await register_user(request.email, request.password)
    return AuthResponse(token=token)


@router.post("/login")
@inject
async def login(
    request: LoginRequest, login_user: FromDishka[LoginUserInteractor]
) -> AuthResponse:
    token = await login_user(request.email, request.password)
    return AuthResponse(token=token)
