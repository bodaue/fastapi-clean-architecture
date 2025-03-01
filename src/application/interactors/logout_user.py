from application.exceptions import AuthenticationRequiredError
from application.interfaces.identity_provider import IdentityProvider
from application.interfaces.request_manager import RequestManager
from application.interfaces.session_repository import SessionRepository
from application.interfaces.transaction_manager import TransactionManager


class LogoutUserInteractor:
    def __init__(
        self,
        session_repository: SessionRepository,
        transaction_manager: TransactionManager,
        request_manager: RequestManager,
        identity_provider: IdentityProvider,
    ) -> None:
        self._session_repository = session_repository
        self._transaction_manager = transaction_manager
        self._request_manager = request_manager
        self._identity_provider = identity_provider

    async def __call__(self) -> None:
        is_authenticated: bool = await self._identity_provider.is_authenticated()
        if not is_authenticated:
            raise AuthenticationRequiredError

        session_id = self._request_manager.get_session_id_from_request()
        await self._session_repository.delete(session_id)
        await self._transaction_manager.commit()

        self._request_manager.delete_session_id_from_request()
