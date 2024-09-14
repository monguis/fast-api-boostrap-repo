from logging_config import generate_logger
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from exception_handlers import (http_exception_handler)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from app.middlewares import error_handling, logging, security, timing


app = FastAPI()

# Prebuilt Middlewares
app.add_middleware(GZipMiddleware, minimum_size=1000) 
app.add_middleware(CORSMiddleware,
    allow_origins=["*"],  # You can specify allowed origins here
    allow_credentials=True,
    allow_methods=["*"],  # You can specify allowed methods here
    allow_headers=["*"],  # You can specify allowed headers here
)
app.add_middleware(logging.CustomLoggingMiddleware)
app.add_middleware(security.SecurityHeadersMiddleware)
app.add_middleware(timing.TimingMiddleware)
app.add_middleware(error_handling.ErrorHandlingMiddleware)

app.add_exception_handler(HTTPException ,http_exception_handler)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    logger = generate_logger("MAIN")
    logger.debug("APP STARTED!!")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)