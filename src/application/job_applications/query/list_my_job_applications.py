from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class ListMyJobApplicationsQuery:
    applicant_id: UUID
