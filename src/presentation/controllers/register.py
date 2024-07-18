from fastapi import APIRouter


def bind_routes():
    router = APIRouter(prefix='/api')
    return router
