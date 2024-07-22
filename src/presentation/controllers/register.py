from fastapi import APIRouter

from src.presentation.controllers.analyze import analyze


def bind_routes():
    router = APIRouter(prefix='/api')
    router.include_router(analyze)
    return router
