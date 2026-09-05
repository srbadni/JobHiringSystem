from dataclasses import dataclass
from typing import Protocol


class AsyncFileReader(Protocol):
    async def read(self, size: int = -1) -> bytes: ...


@dataclass(frozen=True)
class CreateMediaCommand:
    file: AsyncFileReader
    filename: str
    content_type: str | None
    applicant_profile_id: int
