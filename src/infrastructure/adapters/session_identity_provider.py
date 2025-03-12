from datetime import datetime, UTC

from application.interfaces.identity_provider import IdentityProvider
from application.interfaces.request_manager import RequestManager
from application.interfaces.session_repository import SessionRepository
from application.interfaces.user_repository import UserRepository
from domain.entities.user import UserId
from infrastructure.exceptions import AuthenticationError

from domain.entities.session import SessionId, Session


class SessionIdentityProvider(IdentityProvider):
    def __init__(
        self,
        request_manager: RequestManager,
        session_repository: SessionRepository,
        user_repository: UserRepository,
    ) -> None:
        self._request_manager = request_manager
        self._session_repository = session_repository
        self._user_repository = user_repository
        self._current_user_id: UserId | None = None
        self._is_authenticated: bool | None = None

    async def get_current_user_id(self) -> UserId:
        if self._current_user_id is not None:
            return self._current_user_id

        is_auth = await self.is_authenticated()
        if not is_auth or self._current_user_id is None:
            raise AuthenticationError

        return self._current_user_id

    async def is_authenticated(self) -> bool:
        if self._is_authenticated is not None:
            return self._is_authenticated

        session_id: SessionId = self._request_manager.get_session_id_from_request()
        if session_id is None:
            self._is_authenticated = False
            return False

        session: Session = await self._session_repository.get_by_id(session_id)
        if not session:
            self._is_authenticated = False
            return False

        now = datetime.now(UTC)
        if not session.is_active or (session.expires_at and session.expires_at < now):
            self._is_authenticated = False
            return False

        self._current_user_id = session.user_id
        self._is_authenticated = True
        return True
