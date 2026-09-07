from uuid import UUID

from pydantic import BaseModel, Field

from domain.user.enums import UserType
from presentation.http.api.v1.routers.employer.schemas import CompanyCreate


class UserRead(BaseModel):
    id: UUID
    full_name: str
    phone_number: str
    email: str
    profile_image_url: str | None
    user_type: UserType

class UserCreate(BaseModel):
    full_name: str = Field(min_length=3, max_length=90)
    phone_number: str = Field(pattern=r"^\d{11}$")
    email: str = Field(max_length=50)
    password: str = Field(min_length=3)
    profile_image_url: str | None = Field(default=None)
    user_type: UserType = UserType.APPLICANT
    company: CompanyCreate | None = None


class UserUpdate(BaseModel):
    full_name: str = Field(min_length=3, max_length=90)
    phone_number: str = Field(pattern=r"^\d{11}$")
    email: str = Field(max_length=50)
    profile_image_url: str | None = None
