import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from contextlib import asynccontextmanager
from core import settings

@asynccontextmanager
async def lifespan(FastAPI):
    yield

app = FastAPI(lifespan=lifespan,default_response_class=ORJSONResponse)

if __name__=="__main__":
    uvicorn.run(
        "main:app",host=settings.run.host,port=settings.run.port,reload=True
    )