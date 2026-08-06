# app/core/exceptions.py

class AppException(Exception):
    """Base class for all custom application errors."""
    def __init__(self, code: str, message: str, status_code: int = 400):
        self.code = code
        self.message = message
        self.status_code = status_code


class NotFoundException(AppException):
    def __init__(self, message: str = "Resource not found"):
        super().__init__(code="NOT_FOUND", message=message, status_code=404)


class DuplicateException(AppException):
    def __init__(self, message: str = "Resource already exists"):
        super().__init__(code="DUPLICATE", message=message, status_code=400)


class UnauthorizedException(AppException):
    def __init__(self, message: str = "Invalid or missing credentials"):
        super().__init__(code="UNAUTHORIZED", message=message, status_code=401)