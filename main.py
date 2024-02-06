# import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request

from config import initiate_database
from controllers.holiday_controller import route as holiday_router
from middlewares.exception import exception_handler_middleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    await initiate_database()
    yield


app = FastAPI(lifespan=lifespan)


@app.exception_handler(HTTPException)
async def http_exception_handler(request=Request, exc=HTTPException):
    return await exception_handler_middleware(exc, request)


app.include_router(holiday_router, tags=["Holidays"], prefix="/holidays")
