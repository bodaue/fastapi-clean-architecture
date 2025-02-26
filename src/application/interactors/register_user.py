from dataclasses import dataclass
from uuid import UUID

from application.exceptions import UserAlreadyExistsError, InvalidPasswordError
from application.interfaces.transaction_manager import TransactionManager
from application.interfaces.password_hasher import PasswordHasher
from application.interfaces.user_repository import UserRepository
from application.interfaces.uuid_generator import UUIDGenerator
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
        transaction_manager: TransactionManager,
        password_hasher: PasswordHasher,
        id_generator: UUIDGenerator,
    ) -> None:
        self._user_repository = user_repository
        self._transaction_manager = transaction_manager
        self._password_hasher = password_hasher
        self._id_generator = id_generator

    async def __call__(self, data: RegisterUserRequest) -> RegisterUserResponse:
        existing_user = await self._user_repository.get_by_email(data.email)
        if existing_user:
            raise UserAlreadyExistsError(email=data.email)

        user_id = UserId(self._id_generator())
        is_valid_password = validate_password(data.password)
        if not is_valid_password:
            raise InvalidPasswordError

        hashed_password = self._password_hasher.hash(data.password)
        new_user = User(
            id=user_id,
            email=data.email,
            hashed_password=hashed_password,
        )

        created_user = await self._user_repository.create(new_user)
        await self._transaction_manager.commit()
        return RegisterUserResponse(id=created_user.id)
