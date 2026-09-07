from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class CreateJobApplicationCommand:
    applicant_id: UUID
    job_posting_id: UUID
    company_name: str
    folder_id: UUID | None = None
