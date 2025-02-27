from uuid import uuid4

from dishka import Provider, Scope, provide

from application.interfaces.password_hasher import PasswordHasher
from application.interfaces.session_generator import SessionIdGenerator
from application.interfaces.uuid_generator import UUIDGenerator
from infrastructure.adapters.password_hasher import BcryptPasswordHasher
from infrastructure.adapters.session_id_generator import SessionIdGeneratorImpl


class AdapterProvider(Provider):
    @provide(scope=Scope.APP)
    def uuid_generator(self) -> UUIDGenerator:
        return uuid4

    session_id_generator = provide(SessionIdGeneratorImpl, provides=SessionIdGenerator)
    password_hasher = provide(
        BcryptPasswordHasher, provides=PasswordHasher, scope=Scope.APP
    )
