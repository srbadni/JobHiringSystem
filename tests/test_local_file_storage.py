import hashlib
import tempfile
import unittest
from pathlib import Path

from infrastructure.storage.local_file_storage import LocalFileStorage


class MemoryFile:
    def __init__(self, contents: bytes):
        self.contents = contents
        self.offset = 0

    async def read(self, size: int = -1) -> bytes:
        if size < 0:
            size = len(self.contents)
        chunk = self.contents[self.offset:self.offset + size]
        self.offset += len(chunk)
        return chunk


class LocalFileStorageTests(unittest.IsolatedAsyncioTestCase):
    async def test_save_returns_metadata_and_delete_removes_file(self) -> None:
        contents = b"a resume"
        with tempfile.TemporaryDirectory() as directory:
            storage = LocalFileStorage(Path(directory), chunk_size=3)

            result = await storage.save("resumes/file.pdf", MemoryFile(contents))

            self.assertEqual(result.size_bytes, len(contents))
            self.assertEqual(result.checksum_sha256, hashlib.sha256(contents).hexdigest())
            self.assertEqual((Path(directory) / "resumes/file.pdf").read_bytes(), contents)
            await storage.delete("resumes/file.pdf")
            self.assertFalse((Path(directory) / "resumes/file.pdf").exists())

    async def test_save_rejects_empty_files_without_leaving_a_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            storage = LocalFileStorage(Path(directory))

            with self.assertRaisesRegex(ValueError, "must not be empty"):
                await storage.save("resumes/empty.pdf", MemoryFile(b""))

            self.assertFalse((Path(directory) / "resumes/empty.pdf").exists())

    async def test_storage_key_cannot_escape_root(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            storage = LocalFileStorage(Path(directory))

            with self.assertRaisesRegex(ValueError, "storage root"):
                await storage.save("../outside.pdf", MemoryFile(b"resume"))
