from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from redis.asyncio import Redis

from infrastructure.cache.redis_cache import RedisCache
from infrastructure.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    client = Redis.from_url(
        settings.redis_url,
        decode_responses=True,
    )

    app.state.cache = RedisCache(client)

    try:
        yield
    finally:
        await client.aclose()