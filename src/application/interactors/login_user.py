from dataclasses import dataclass

from application.exceptions import InvalidCredentialsError
from application.interfaces.password_hasher import PasswordHasher
from application.interfaces.token_processor import TokenProcessor
from application.interfaces.user_repository import UserRepository


@dataclass
class LoginUserRequest:
    email: str
    password: str


@dataclass
class LoginUserResponse:
    access_token: str


class LoginUserInteractor:
    def __init__(
        self,
        user_repository: UserRepository,
        token_processor: TokenProcessor,
        password_hasher: PasswordHasher,
    ) -> None:
        self.user_repository = user_repository
        self.token_processor = token_processor
        self.password_hasher = password_hasher

    async def __call__(self, data: LoginUserRequest) -> LoginUserResponse:
        user = await self.user_repository.get_by_email(data.email)
        if not user:
            raise InvalidCredentialsError
        user.ensure_is_active()

        if not self.password_hasher.verify(data.password, user.hashed_password):
            raise InvalidCredentialsError

        access_token = self.token_processor.create_access_token(user.id)
        return LoginUserResponse(access_token=access_token)
