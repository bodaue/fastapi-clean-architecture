from dishka import Provider, Scope, from_context

from main.config import Config


class ServiceProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)
