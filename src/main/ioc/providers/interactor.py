from dishka import Provider, provide, Scope

from application.interactors.login_user import LoginUserInteractor
from application.interactors.register_user import RegisterUserInteractor


class InteractorProvider(Provider):
    scope = Scope.REQUEST
    register_user = provide(RegisterUserInteractor)
    login_user = provide(LoginUserInteractor)
