from typing import Protocol


class CachePort(Protocol):
    async def get(self, key: str) -> bytes | str | None:
        ...

    async def set(
        self,
        key: str,
        value: str,
        *,
        ttl_seconds: int,
    ) -> None:
        ...

    async def delete(self, key: str) -> None:
        ...