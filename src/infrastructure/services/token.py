from datetime import timedelta, datetime, UTC
from typing import Literal

from jose import jwt, JWTError

from application.interfaces.id_provider import IdProvider
from application.interfaces.token_processor import TokenProcessor
from domain.entities.user import UserId
from infrastructure.exceptions import AuthenticationError

type Algorithm = Literal[
    "HS256",
    "HS384",
    "HS512",
    "RS256",
    "RS384",
    "RS512",
]


class JwtTokenProcessor(TokenProcessor):
    def __init__(
        self,
        secret: str,
        expires: timedelta,
        algorithm: Algorithm,
    ) -> None:
        self.secret = secret
        self.expires = expires
        self.algorithm = algorithm

    def create_access_token(
        self,
        user_id: UserId,
    ) -> str:
        to_encode = {"sub": str(user_id)}
        expire = datetime.now(UTC) + self.expires
        to_encode["exp"] = expire
        return jwt.encode(
            to_encode,
            self.secret,
            algorithm=self.algorithm,
        )

    def validate_token(self, token: str) -> UserId:
        try:
            payload = jwt.decode(
                token,
                self.secret,
                algorithms=[self.algorithm],
            )
        except JWTError as e:
            raise AuthenticationError from e

        try:
            return UserId(int(payload["sub"]))
        except ValueError as e:
            raise AuthenticationError from e


class TokenIdProvider(IdProvider):
    def __init__(
        self,
        token_processor: JwtTokenProcessor,
        token: str,
    ) -> None:
        self.token_processor = token_processor
        self.token = token

    def get_current_user_id(self) -> UserId:
        return self.token_processor.validate_token(self.token)
