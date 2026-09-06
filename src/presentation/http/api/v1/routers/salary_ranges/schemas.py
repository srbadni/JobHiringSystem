from uuid import UUID

from pydantic import BaseModel, Field, model_validator


class SalaryRangeCreate(BaseModel):
    title: str = Field(min_length=1)
    min_salary: int | None = Field(default=None, ge=0)
    max_salary: int | None = Field(default=None, ge=0)

    @model_validator(mode="after")
    def validate_salary_bounds(self) -> "SalaryRangeCreate":
        if self.min_salary is not None and self.max_salary is not None and self.min_salary > self.max_salary:
            raise ValueError("min_salary must be less than or equal to max_salary")
        return self


class SalaryRangeRead(BaseModel):
    id: UUID
    title: str
    min_salary: int | None
    max_salary: int | None


class SalaryRangeUpdate(SalaryRangeCreate):
    pass
