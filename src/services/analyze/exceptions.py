from src.services.common.exceptions import BusinessException


class NotFoundHistory(BusinessException):
    code = 404
    message = "History not found"
    error_code = "NOT_FOUND_HISTORY"


class NoVideoStream(BusinessException):
    code = 404
    message = "No video stream"
    error_code = "NO_VIDEO_STREAM"
