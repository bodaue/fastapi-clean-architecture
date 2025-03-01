from fastapi import Request

from application.interfaces.request_manager import RequestManager
from domain.entities.session import SessionId
from main.config import SessionConfig


class FastAPIRequestManager(RequestManager):
    def __init__(self, request: Request, session_config: SessionConfig) -> None:
        self._request = request
        self._config = session_config

    def get_session_id_from_request(self) -> SessionId | None:
        session_id = self._request.cookies.get(self._config.cookie_name)
        if not session_id:
            return None
        return SessionId(session_id)

    def add_session_id_to_request(self, session_id: SessionId) -> None:
        self._request.state.session_id = session_id

    def delete_session_id_from_request(self) -> None:
        self._request.state.delete_session_id = True
