from dishka import Provider, Scope, provide

from application.interfaces.session_repository import SessionRepository
from application.interfaces.user_repository import UserRepository
from infrastructure.database.repositories.session import SQLSessionRepository
from infrastructure.database.repositories.user import SQLUserRepository


class RepositoryProvider(Provider):
    scope = Scope.REQUEST

    user_repository = provide(SQLUserRepository, provides=UserRepository)
    session_repository = provide(SQLSessionRepository, provides=SessionRepository)
