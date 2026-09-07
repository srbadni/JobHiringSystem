from uuid import UUID

from pydantic import BaseModel, Field


class CompanyActivityCreate(BaseModel):
    code: str = Field(min_length=1)
    title: str = Field(min_length=1)


class CompanyActivityRead(BaseModel):
    id: UUID
    code: str
    title: str


class CompanyActivityUpdate(CompanyActivityCreate):
    pass
