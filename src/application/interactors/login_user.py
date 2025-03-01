from dataclasses import dataclass
from datetime import datetime, UTC

from asyncpg.pgproto.pgproto import timedelta

from application.exceptions import InvalidCredentialsError, LogInError
from application.interfaces.session_generator import SessionIdGenerator
from application.interfaces.transaction_manager import TransactionManager
from application.interfaces.identity_provider import IdentityProvider
from application.interfaces.password_hasher import PasswordHasher
from application.interfaces.request_manager import RequestManager
from application.interfaces.session_repository import SessionRepository
from application.interfaces.user_repository import UserRepository
from domain.entities.session import SessionId, Session
from main.config import SessionConfig


@dataclass
class LoginUserRequest:
    email: str
    password: str


class LoginUserInteractor:
    def __init__(
        self,
        user_repository: UserRepository,
        session_repository: SessionRepository,
        transaction_manager: TransactionManager,
        password_hasher: PasswordHasher,
        session_id_generator: SessionIdGenerator,
        request_manager: RequestManager,
        identity_provider: IdentityProvider,
        session_config: SessionConfig,
    ) -> None:
        self._user_repository = user_repository
        self._session_repository = session_repository
        self._transaction_manager = transaction_manager
        self._password_hasher = password_hasher
        self._session_id_generator = session_id_generator
        self._request_manager = request_manager
        self._identity_provider = identity_provider
        self._session_config = session_config

    async def __call__(self, data: LoginUserRequest) -> None:
        is_authenticated: bool = await self._identity_provider.is_authenticated()
        if is_authenticated:
            raise LogInError

        user = await self._user_repository.get_by_email(data.email)
        if not user:
            raise InvalidCredentialsError
        user.ensure_is_active()

        if not self._password_hasher.verify(data.password, user.hashed_password):
            raise InvalidCredentialsError

        session_id: SessionId = self._session_id_generator()
        expires_at = datetime.now(UTC) + timedelta(
            minutes=self._session_config.lifetime_minutes
        )
        session: Session = Session(
            id=session_id, user_id=user.id, expires_at=expires_at
        )
        await self._session_repository.create(session)
        await self._transaction_manager.commit()

        self._request_manager.add_session_id_to_request(session.id)
