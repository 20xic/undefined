import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from contextlib import asynccontextmanager
from core import settings,logger


@asynccontextmanager
async def lifespan(FastAPI):
    logger.info("Aplication starting...")
    yield
    logger.info("Aplication shuting down...")

app = FastAPI(lifespan=lifespan,default_response_class=ORJSONResponse)

if __name__=="__main__":
    uvicorn.run(
        "main:app",host=settings.run.host,port=settings.run.port,reload=True
    )