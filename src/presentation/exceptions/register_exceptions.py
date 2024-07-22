from fastapi import FastAPI

from src.presentation.exceptions.handler import (

    not_found_handler,
)
from src.services.analyze.exceptions import NotFoundHistory, NoVideoStream


def register_exception_handler(app: FastAPI):
    app.exception_handlers.setdefault(  # noqa
        NotFoundHistory, not_found_handler,
    )
    app.exception_handlers.setdefault(  # noqa
        NoVideoStream, not_found_handler,
    )

