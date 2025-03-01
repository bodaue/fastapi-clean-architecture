from collections.abc import Callable, Awaitable

from starlette.requests import Request
from starlette.responses import Response

from main.config import SessionConfig


class SessionMiddleware:
    def __init__(self, session_config: SessionConfig) -> None:
        self._config = session_config

    async def __call__(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        response = await call_next(request)

        if hasattr(request.state, "session_id"):
            session_id = request.state.session_id
            response.set_cookie(
                key=self._config.cookie_name,
                value=session_id,
                max_age=self._config.lifetime_minutes,
                path=self._config.path,
                domain=self._config.domain,
                secure=self._config.secure,
                samesite=self._config.samesite,
                httponly=True,
            )

        if (
            hasattr(request.state, "delete_session_id")
            and request.state.delete_session_id
        ):
            response.delete_cookie(
                key=self._config.cookie_name,
                path=self._config.path,
                domain=self._config.domain,
            )

        return response
