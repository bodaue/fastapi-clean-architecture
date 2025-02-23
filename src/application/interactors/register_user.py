from dataclasses import dataclass
from uuid import UUID

from application.exceptions import UserAlreadyExistsError, InvalidPasswordError
from application.interfaces.committer import Committer
from application.interfaces.id_generator import IdGenerator
from application.interfaces.password_hasher import PasswordHasher
from application.interfaces.user_repository import UserRepository
from application.validators import validate_password
from domain.entities.user import User, UserId


@dataclass
class RegisterUserRequest:
    email: str
    password: str


@dataclass
class RegisterUserResponse:
    id: UUID


class RegisterUserInteractor:
    def __init__(
        self,
        user_repository: UserRepository,
        committer: Committer,
        password_hasher: PasswordHasher,
        id_generator: IdGenerator,
    ) -> None:
        self.user_repository = user_repository
        self.committer = committer
        self.password_hasher = password_hasher
        self.id_generator = id_generator

    async def __call__(self, data: RegisterUserRequest) -> RegisterUserResponse:
        existing_user = await self.user_repository.get_by_email(data.email)
        if existing_user:
            raise UserAlreadyExistsError(email=data.email)

        user_id = UserId(self.id_generator())
        is_valid_password = validate_password(data.password)
        if not is_valid_password:
            raise InvalidPasswordError

        hashed_password = self.password_hasher.hash(data.password)
        new_user = User(
            id=user_id,
            email=data.email,
            hashed_password=hashed_password,
        )

        created_user = await self.user_repository.create(new_user)
        await self.committer.commit()
        return RegisterUserResponse(id=created_user.id)
