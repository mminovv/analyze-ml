from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.infra.di.container import get_container
from src.presentation.controllers.register import bind_routes
from src.presentation.exceptions.register_exceptions import register_exception_handler


def initialize_app(_app: FastAPI) -> FastAPI:
    _app.include_router(bind_routes())
    register_exception_handler(_app)
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

