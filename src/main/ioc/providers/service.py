from dishka import Provider, provide, Scope, from_context

from application.interfaces.password_hasher import PasswordHasher
from infrastructure.adapters.password_hasher import BcryptPasswordHasher
from main.config import Config


class ServiceProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)

    password_hasher = provide(
        BcryptPasswordHasher, provides=PasswordHasher, scope=Scope.APP
    )
