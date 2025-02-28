from fastapi import Request

from application.interfaces.request_manager import RequestManager
from domain.entities.session import SessionId


class FastAPIRequestManager(RequestManager):
    SESSION_COOKIE_NAME = "session_id"
    SESSION_STATE_KEY = "session_id"

    def __init__(self, request: Request) -> None:
        self.request = request

    def get_session_id_from_request(self) -> SessionId | None:
        session_id = self.request.cookies.get(self.SESSION_COOKIE_NAME)
        if not session_id:
            return None
        return SessionId(session_id)

    def add_session_id_to_request(self, session_id: SessionId) -> None:
        self.request.state.session_id = session_id
