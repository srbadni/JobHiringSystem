from dataclasses import dataclass
from uuid import UUID


@dataclass
class GetJobDetailsQuery:
    job_posting_id: UUID
    company_en_name: str