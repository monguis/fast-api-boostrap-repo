from fastapi import Request, HTTPException
from logging_config import generateLoger
from fastapi.responses import JSONResponse
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_405_METHOD_NOT_ALLOWED,
    HTTP_500_INTERNAL_SERVER_ERROR
)

async def http_exception_handler(request: Request, exc: HTTPException):
    logger = generateLoger("error")
    
    error_type = ""
    
    # Log different messages based on the exception type
    if isinstance(exc, BadRequestException):
        error_type = "Bad Request Error"
    elif isinstance(exc, NotFoundException):
        error_type = "Not Found"
    elif isinstance(exc, UnauthorizedException):
        error_type = "Unauthorized"
    elif isinstance(exc, ForbiddenException):
        error_type = "Forbidden"
    elif isinstance(exc, MethodNotAllowedException):
        error_type = "Method Not Allowed"
    elif isinstance(exc, InternalServerErrorException):
        error_type = "Internal Server Error"
    else:
        error_type = "Unexpected Error"
    
    logger.warning(f"{error_type}: {exc.detail}, Path: {request.url.path}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail, "type": "HTTPException"}
    )



class BadRequestException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=HTTP_400_BAD_REQUEST, detail=detail)
        
class UnauthorizedException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=HTTP_401_UNAUTHORIZED, detail=detail)
        
class ForbiddenException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=HTTP_403_FORBIDDEN, detail=detail)
        
class NotFoundException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=HTTP_404_NOT_FOUND, detail=detail)
        
class MethodNotAllowedException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=HTTP_405_METHOD_NOT_ALLOWED, detail=detail)

class InternalServerErrorException(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)
        
