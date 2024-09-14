from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from fastapi import Request
from logging_config import generate_logger

error_logger = generate_logger("ERROR")
class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
        except Exception as exc:
            error_logger.error(f"{500}: UNEXPECTED ERROR, Path: {request.url.path}")
            return JSONResponse(
                status_code=500,
                content={"detail": str(exc)}
            )
        return response