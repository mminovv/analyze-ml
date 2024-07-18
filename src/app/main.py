from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.infra.di.container import get_container


def initialize_app(_app: FastAPI) -> FastAPI:
    container = get_container()
    setup_dishka(container, _app)
    return _app


app = initialize_app(
    FastAPI(
        title="Analyzers API",
        version="0.1.0",
        description="Image or Video processing API with ML models.",
    ),
)

