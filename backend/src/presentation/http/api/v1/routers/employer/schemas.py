from uuid import UUID
from typing import Annotated

from pydantic import BaseModel, Field, field_validator, ConfigDict

from domain.company.enums import EmployeeCount

class EmployerCreate(BaseModel):
    full_name: str = Field(min_length=3, max_length=90)
    phone_number: str = Field(pattern=r"^\d{11}$")
    email: str = Field(max_length=50)
    password: str = Field(min_length=3)
    profile_image_url: str | None = Field(default=None)

class EmployerRead(BaseModel):
    full_name: str
    phone_number: str
    email: str
    profile_image_url: str | None = None

class CompanyCreate(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=120)]
    persian_name: Annotated[str, Field(min_length=2, max_length=120)]
    province_id: UUID
    city_id: UUID
    activity_id: UUID
    personnel_count: Annotated[EmployeeCount, Field()]
    logo_path: str | None = None
    phone_number: Annotated[
        str,
        Field(
            pattern=r"^09\d{9}$",
            examples=["09123456789"],
            description="Iranian mobile number in 09XXXXXXXXX format",
        ),
    ]
    description: Annotated[str | None, Field(max_length=2000)] = None
    website: str | None = None

    @field_validator("name", mode="before")
    @classmethod
    def strip_and_validate_name(cls, value: object) -> object:
        if isinstance(value, str):
            value = value.strip()
            if not value:
                raise ValueError("name must not be blank")
        return value

class CompanyRead(CompanyCreate):
    id: UUID

    model_config = ConfigDict(from_attributes=True)

class EmployerCompanyCreate(BaseModel):
    employer: EmployerCreate
    company: CompanyCreate