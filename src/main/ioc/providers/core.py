from dishka import Provider, provide, Scope, from_context

from main.config import Config, SessionConfig, PostgresConfig, RedisConfig


class ConfigProvider(Provider):
    scope = Scope.APP
    config = from_context(provides=Config)

    @provide
    def get_session_config(self, config: Config) -> SessionConfig:
        return config.session

    @provide
    def get_postgres_config(self, config: Config) -> PostgresConfig:
        return config.postgres

    @provide
    def get_redis_config(self, config: Config) -> RedisConfig:
        return config.redis
