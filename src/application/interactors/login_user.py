from application.interfaces.password_hasher import PasswordHasher
from application.interfaces.user_repository import UserRepository
from domain.exceptions.access import AuthenticationError
from infrastructure.services.token import JwtTokenProcessor


class LoginUserInteractor:
    def __init__(
        self,
        user_repository: UserRepository,
        token_processor: JwtTokenProcessor,
        password_hasher: PasswordHasher,
    ) -> None:
        self.user_repository = user_repository
        self.token_processor = token_processor
        self.password_hasher = password_hasher

    async def __call__(self, email: str, password: str) -> str:
        user = await self.user_repository.get_by_email(email)
        if not user:
            raise AuthenticationError("Invalid credentials")

        if not self.password_hasher.verify(password, user.hashed_password):
            raise AuthenticationError("Invalid credentials")

        return self.token_processor.create_access_token(user.id)
