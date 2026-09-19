from redis.asyncio import Redis

from application.common.ports.cache import CachePort


class RedisCache(CachePort):
    def __init__(self, client: Redis) -> None:
        self._client = client

    async def get(self, key: str) -> bytes | str | None:
        return await self._client.get(key)

    async def set(
        self,
        key: str,
        value: str,
        *,
        ttl_seconds: int,
    ) -> None:
        await self._client.set(
            name=key,
            value=value,
            ex=ttl_seconds,
        )

    async def delete(self, key: str) -> None:
        await self._client.delete(key)