from starlette.middleware.base import BaseHTTPMiddleware
from logging_config import generate_logger

logger = generate_logger("REQUEST")

class CustomLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        logger.info(f"Request: {request.method} {request.url}")
        response = await call_next(request)
        logger.info(f"Response: {response.status_code}")
        return response