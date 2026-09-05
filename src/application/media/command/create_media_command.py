from dataclasses import dataclass
from typing import Protocol
from uuid import UUID


class AsyncFileReader(Protocol):
    async def read(self, size: int = -1) -> bytes: ...


@dataclass(frozen=True)
class CreateMediaCommand:
    file: AsyncFileReader
    filename: str
    content_type: str | None
    applicant_profile_id: UUID
