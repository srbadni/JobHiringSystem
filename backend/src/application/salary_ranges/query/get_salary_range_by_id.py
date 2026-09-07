from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class GetSalaryRangeByIdQuery:
    salary_range_id: UUID
