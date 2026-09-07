from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class GetJobPostingByIdQuery:
    job_posting_id: UUID
    company_id: UUID
