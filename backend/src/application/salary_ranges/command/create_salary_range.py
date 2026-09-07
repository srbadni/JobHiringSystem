from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CreateSalaryRangeCommand:
    title: str
    min_salary: int | None
    max_salary: int | None
