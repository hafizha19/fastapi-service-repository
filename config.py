import asyncio
import logging
from datetime import datetime
from mongoengine import connect
from pydantic_settings import BaseSettings

loop = asyncio.get_event_loop()


class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env.dev"


async def initiate_database():
    client = connect(host=Settings().DATABASE_URL)
    return client


# Configure logging
logging.basicConfig(
    filename=f'logs\log_{datetime.now().strftime("%Y-%m-%d")}.log',
    level=logging.INFO,  # Set the logging level according to your needs
    format="%(levelname)s - %(message)s - Line %(lineno)d - %(asctime)s",
)

# Define a logger for your FastAPI app
logger = logging.getLogger(__name__)
