import asyncio
import hashlib
from pathlib import Path

from application.media.command.create_media_command import AsyncFileReader
from application.media.ports.file_storage import FileStorage, StoredFile


class LocalFileStorage(FileStorage):
    """Store private files beneath a configured local directory."""

    def __init__(self, root: Path, chunk_size: int = 1024 * 1024):
        self.root = root.resolve()
        self.chunk_size = chunk_size

    async def save(self, storage_key: str, source: AsyncFileReader) -> StoredFile:
        destination = self._destination(storage_key)
        await asyncio.to_thread(destination.parent.mkdir, parents=True, exist_ok=True)
        checksum = hashlib.sha256()
        size_bytes = 0

        try:
            with destination.open("xb") as output:
                while chunk := await source.read(self.chunk_size):
                    size_bytes += len(chunk)
                    checksum.update(chunk)
                    await asyncio.to_thread(output.write, chunk)
            if size_bytes == 0:
                raise ValueError("Uploaded file must not be empty.")
        except BaseException:
            await asyncio.to_thread(destination.unlink, missing_ok=True)
            raise

        return StoredFile(size_bytes=size_bytes, checksum_sha256=checksum.hexdigest())

    async def delete(self, storage_key: str) -> None:
        await asyncio.to_thread(self._destination(storage_key).unlink, missing_ok=True)

    def _destination(self, storage_key: str) -> Path:
        destination = (self.root / storage_key).resolve()
        if not destination.is_relative_to(self.root):
            raise ValueError("Storage key must remain within the storage root.")
        return destination
