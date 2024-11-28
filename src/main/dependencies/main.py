from dishka import AsyncContainer, make_async_container


def container_factory() -> AsyncContainer:
    return make_async_container()
