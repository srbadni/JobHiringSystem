from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class UpdateJobCategoryCommand:
    job_category_id: UUID
    code: str
    title: str
