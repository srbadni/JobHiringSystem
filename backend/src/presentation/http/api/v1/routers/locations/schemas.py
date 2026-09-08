from uuid import UUID

from pydantic import BaseModel


class ProvinceRead(BaseModel):
    id: UUID
    name: str
    english_name: str


class CityRead(BaseModel):
    id: UUID
    name: str
    english_name: str
    province_id: UUID
