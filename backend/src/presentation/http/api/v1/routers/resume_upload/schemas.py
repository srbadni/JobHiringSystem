from uuid import UUID
from pydantic import BaseModel


class ResumeUploadRead(BaseModel):
    id: UUID
    original_name: str
    storage_key: str
    mime_type: str
    size_bytes: int
    checksum_sha256: str
