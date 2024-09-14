import time
from starlette.middleware.base import BaseHTTPMiddleware
from logging_config import generate_logger
from math import ceil
        
time_logger = generate_logger("TIME")
class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        
        time_logger.info(f"Time to execute: {ceil(process_time*1000000)}µs, Path: {request.url.path}")
        response.headers['X-Process-Time'] = str(process_time)
        return response