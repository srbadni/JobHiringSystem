from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class GetJobCategoryByIdQuery:
    job_category_id: UUID
