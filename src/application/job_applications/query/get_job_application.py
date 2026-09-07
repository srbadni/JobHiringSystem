from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class GetJobApplicationQuery:
    application_id: UUID
    applicant_id: UUID
