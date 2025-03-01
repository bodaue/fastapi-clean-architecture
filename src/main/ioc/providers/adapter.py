from uuid import uuid4

from dishka import Provider, Scope, provide

from application.interfaces.identity_provider import IdentityProvider
from application.interfaces.password_hasher import PasswordHasher
from application.interfaces.request_manager import RequestManager
from application.interfaces.session_generator import SessionIdGenerator
from application.interfaces.uuid_generator import UUIDGenerator
from infrastructure.adapters.fastapi_request_manager import FastAPIRequestManager
from infrastructure.adapters.password_hasher import BcryptPasswordHasher
from infrastructure.adapters.session_id_generator import SessionIdGeneratorImpl
from infrastructure.adapters.session_identity_provider import SessionIdentityProvider


class AdapterProvider(Provider):
    @provide(scope=Scope.APP)
    def uuid_generator(self) -> UUIDGenerator:
        return uuid4

    session_id_generator = provide(
        SessionIdGeneratorImpl, provides=SessionIdGenerator, scope=Scope.REQUEST
    )
    password_hasher = provide(
        BcryptPasswordHasher, provides=PasswordHasher, scope=Scope.APP
    )
    request_manager = provide(
        FastAPIRequestManager, provides=RequestManager, scope=Scope.REQUEST
    )
    identity_provider = provide(
        SessionIdentityProvider, provides=IdentityProvider, scope=Scope.REQUEST
    )
