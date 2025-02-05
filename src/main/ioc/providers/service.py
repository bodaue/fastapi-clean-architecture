from datetime import timedelta

from dishka import Provider, provide, Scope, from_context

from application.interfaces.password_hasher import PasswordHasher
from application.interfaces.token_processor import TokenProcessor
from infrastructure.adapters.password_hasher import BcryptPasswordHasher
from infrastructure.adapters.token import JwtTokenProcessor
from main.config import Config


class ServiceProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)

    password_hasher = provide(
        BcryptPasswordHasher, provides=PasswordHasher, scope=Scope.APP
    )

    @provide(scope=Scope.APP)
    def get_token_processor(self, config: Config) -> TokenProcessor:
        expires = timedelta(minutes=config.jwt.access_token_expires_minutes)
        return JwtTokenProcessor(
            secret=config.jwt.secret_key.get_secret_value(),
            expires=expires,
            algorithm=config.jwt.algorithm,
        )
