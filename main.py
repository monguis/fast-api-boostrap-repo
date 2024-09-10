from logging_config import generateLoger
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from exception_handlers import (http_exception_handler, NotFoundException)

app = FastAPI()

# logging.basicConfig(level=logging.DEBUG, filename='./logs/app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

app.add_exception_handler(HTTPException ,http_exception_handler)
@app.get("/")
async def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    logger = generateLoger("main")
    logger.debug("APP STARTED!!")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)