from uuid import UUID

from pydantic import BaseModel, Field


class JobCategoryCreate(BaseModel):
    code: str = Field(min_length=1)
    title: str = Field(min_length=1)


class JobCategoryRead(BaseModel):
    id: UUID
    code: str
    title: str


class JobCategoryUpdate(JobCategoryCreate):
    pass
