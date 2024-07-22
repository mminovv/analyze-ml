from fastapi import (
    Request,
    status,
)
from fastapi.responses import JSONResponse

from src.services.common.exceptions import BusinessException


async def not_found_handler(request: Request, exc: BusinessException) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content=dict(message=exc.message, code=exc.code)
    )


async def logic_error_handler(request: Request, exc: BusinessException) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, content=dict(message=exc.message, code=exc.code)
    )