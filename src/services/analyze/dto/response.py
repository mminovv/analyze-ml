from uuid import UUID

from pydantic import BaseModel


class AnalyzeResponseModel(BaseModel):
    request_id: UUID


class GetAnalyzeResponseModel(BaseModel):
    result: list[dict]
