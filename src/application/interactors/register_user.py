from sqlalchemy.ext.asyncio import AsyncSession

from application.interfaces.password_hasher import PasswordHasher
from application.interfaces.token_processor import TokenProcessor
from application.interfaces.user_repository import UserRepository
from domain.entities.user import User


class RegisterUserInteractor:
    def __init__(
        self,
        user_repository: UserRepository,
        password_hasher: PasswordHasher,
        token_processor: TokenProcessor,
        session: AsyncSession,
    ) -> None:
        self.user_repository = user_repository
        self.password_hasher = password_hasher
        self.token_processor = token_processor
        self.session = session

    async def __call__(self, email: str, password: str) -> str:
        existing_user = await self.user_repository.get_by_email(email)
        if existing_user:
            raise ValueError("User already exists")
        hashed_password = self.password_hasher.hash(password)
        new_user = User(
            id=None,
            email=email,
            hashed_password=hashed_password,
        )
        created_user = await self.user_repository.create(new_user)
        await self.session.commit()
        return self.token_processor.create_access_token(created_user.id)
