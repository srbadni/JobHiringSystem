from dataclasses import dataclass


@dataclass
class MediaDTO:
    original_name: str
    storage_key: str
    mime_type: str
    size_bytes: int
    checksum_sha256: str
    id: int | None = None