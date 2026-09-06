from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(slots=True)
class SalaryRange:
    title: str
    min_salary: int | None
    max_salary: int | None
    id: UUID = field(default_factory=uuid4)
