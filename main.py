# import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware

from config import initiate_database
from controllers.holiday_controller import route as holiday_router
from middlewares.exception import exception_handler_middleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    await initiate_database()
    yield


app = FastAPI(lifespan=lifespan)

# Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(HTTPException)
async def http_exception_handler(request=Request, exc=HTTPException):
    return await exception_handler_middleware(exc, request)


@app.middleware("http")
async def add_default_headers(request, call_next):
    response = await call_next(request)
    response.headers.update(
        {
            "Access-Control-Allow-Headers": "Content-Type, Accept, X-Requested-With",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
        }
    )
    return response


app.include_router(holiday_router, tags=["Holidays"], prefix="/holidays")
