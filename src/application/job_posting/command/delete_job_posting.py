from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class DeleteJobPostingCommand:
    job_posting_id: UUID
