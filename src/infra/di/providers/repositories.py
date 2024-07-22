from dishka import (
    Provider,
    provide,
)

from src.infra.db.repositories.analyze_history import AnalyzeHistoryImpl
from src.interfaces.repositories.db.analyze_history import AnalyzeHistoryRepository


class RepositoryProvider(Provider):
    analyze_history_repository = provide(AnalyzeHistoryImpl, provides=AnalyzeHistoryRepository)
