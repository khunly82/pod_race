from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
import os

from core.app_utils import add_controllers, add_exception_handlers

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

load_dotenv()

@asynccontextmanager
async def lifespan(_: FastAPI):
    redis = aioredis.from_url(os.getenv('REDIS_URL'))
    FastAPICache.init(RedisBackend(redis), prefix='pod_api')
    yield

app = FastAPI(lifespan=lifespan)

add_controllers(app)
add_exception_handlers(app)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)