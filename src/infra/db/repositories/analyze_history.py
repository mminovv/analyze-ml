from uuid import UUID

from sqlalchemy import select

from src.infra.db.models.analyze import AnalyzeHistory
from src.interfaces.db import get_session
from src.interfaces.repositories.db.analyze_history import AnalyzeHistoryRepository


class AnalyzeHistoryImpl(AnalyzeHistoryRepository):
    def __init__(self, session: get_session):
        self.session = session

    async def save(self, analyze_history: AnalyzeHistory) -> AnalyzeHistory:
        self.session.add(analyze_history)
        await self.session.commit()
        return analyze_history

    async def get_analyze_by_id(self, request_id: UUID) -> AnalyzeHistory:
        query = (
            select(AnalyzeHistory)
            .where(AnalyzeHistory.id == request_id)
        )
        result = await self.session.execute(query)
        return result.scalars().one_or_none()

    async def delete_analyze_history(self, request_id: UUID) -> None:
        query = (
            select(AnalyzeHistory)
            .filter(AnalyzeHistory.id.is_(request_id))
        )
        result = self.session.execute(query)
        self.session.delete(result.scalar().first())
        self.session.commit()
