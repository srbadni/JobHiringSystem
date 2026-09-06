from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class DeleteJobCategoryCommand:
    job_category_id: UUID
