from sqlalchemy import Column, JSON

from src.infra.db.models.common import Base


class AnalyzeHistory(Base):
    __tablename__ = 't_analyze_history'

    result = Column(JSON, nullable=True)
