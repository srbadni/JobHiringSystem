from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GetJobPostingByIdQuery:
    job_posting_id: int
