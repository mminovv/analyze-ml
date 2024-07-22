from abc import ABC, abstractmethod
from uuid import UUID

from src.infra.db.models.analyze import AnalyzeHistory


class AnalyzeHistoryRepository(ABC):
    @abstractmethod
    async def save(self, analyze_history: AnalyzeHistory) -> AnalyzeHistory:
        raise NotImplementedError

    @abstractmethod
    async def get_analyze_by_id(self, request_id: UUID) -> AnalyzeHistory:
        raise NotImplementedError

    @abstractmethod
    async def delete_analyze_history(self, request_id: UUID) -> None:
        raise NotImplementedError
