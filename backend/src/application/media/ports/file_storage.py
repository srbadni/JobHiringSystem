from abc import ABC, abstractmethod
from dataclasses import dataclass

from application.media.command.create_media_command import AsyncFileReader


@dataclass(frozen=True)
class StoredFile:
    size_bytes: int
    checksum_sha256: str


class FileStorage(ABC):
    """Persistence boundary for private file contents."""

    @abstractmethod
    async def save(self, storage_key: str, source: AsyncFileReader) -> StoredFile:
        """Persist source under storage_key and return properties of its contents."""

    @abstractmethod
    async def delete(self, storage_key: str) -> None:
        """Delete storage_key when present."""
