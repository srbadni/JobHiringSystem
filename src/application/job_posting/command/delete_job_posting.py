from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DeleteJobPostingCommand:
    job_posting_id: int
