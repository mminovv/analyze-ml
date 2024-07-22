from dishka import (
    Provider, provide,
)

from src.services.analyze.use_case import AnalyzeService, GetAnalyzeByRequestIdService, DeleteAnalyzeByRequestIdService


class ServiceProvider(Provider):
    analytics_service = provide(AnalyzeService)
    get_analytics_service = provide(GetAnalyzeByRequestIdService)
    delete_analytics_service = provide(DeleteAnalyzeByRequestIdService)

