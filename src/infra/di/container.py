from dishka import (
    AsyncContainer, Scope,
)
from dishka import (
    make_async_container,
)

from src.infra.di.providers.repositories import RepositoryProvider
from src.infra.di.providers.service import ServiceProvider
from src.infra.di.providers.session import SessionProvider, SessionProviderArq


def get_container() -> AsyncContainer:
    service_provider = ServiceProvider(scope=Scope.REQUEST)
    repository_provider = RepositoryProvider(scope=Scope.REQUEST)
    session_provider = SessionProvider()

    return make_async_container(
        session_provider,
        service_provider,
        repository_provider,
    )


def get_arq_container() -> AsyncContainer:
    repository_provider = RepositoryProvider(scope=Scope.APP)
    service_provider = ServiceProvider(scope=Scope.APP)
    session_provider = SessionProviderArq()

    return make_async_container(
        session_provider,
        service_provider,
        repository_provider,
    )