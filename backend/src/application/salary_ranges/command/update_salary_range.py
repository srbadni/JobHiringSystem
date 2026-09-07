from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class UpdateSalaryRangeCommand:
    salary_range_id: UUID
    title: str
    min_salary: int | None
    max_salary: int | None
