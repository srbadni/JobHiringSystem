from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class Province:
    id: UUID
    name: str
    english_name: str


@dataclass(frozen=True, slots=True)
class City:
    id: UUID
    name: str
    english_name: str
    province_id: UUID
