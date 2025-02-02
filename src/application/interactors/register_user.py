from application.exceptions import UserAlreadyExistsError
from application.interfaces.committer import Committer
from application.interfaces.password_hasher import PasswordHasher
from application.interfaces.token_processor import TokenProcessor
from application.interfaces.user_repository import UserRepository
from domain.entities.user import User


class RegisterUserInteractor:
    def __init__(
        self,
        user_repository: UserRepository,
        committer: Committer,
        password_hasher: PasswordHasher,
        token_processor: TokenProcessor,
    ) -> None:
        self.user_repository = user_repository
        self.committer = committer
        self.password_hasher = password_hasher
        self.token_processor = token_processor

    async def __call__(self, email: str, password: str) -> str:
        existing_user = await self.user_repository.get_by_email(email)
        if existing_user:
            raise UserAlreadyExistsError(email=email)
        hashed_password = self.password_hasher.hash(password)
        new_user = User(
            id=None,
            email=email,
            hashed_password=hashed_password,
        )
        created_user = await self.user_repository.create(new_user)
        await self.committer.commit()
        return self.token_processor.create_access_token(created_user.id)
