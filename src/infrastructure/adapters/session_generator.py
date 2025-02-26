from secrets import token_urlsafe

from application.interfaces.session_generator import SessionIdGenerator


class SessionIdGeneratorImpl(SessionIdGenerator):
    def __call__(self) -> str:
        return token_urlsafe(128)
