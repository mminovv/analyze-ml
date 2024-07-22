from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.infra.di.container import get_container
from src.presentation.controllers.register import bind_routes


def initialize_app(_app: FastAPI) -> FastAPI:
    _app.include_router(bind_routes())
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

