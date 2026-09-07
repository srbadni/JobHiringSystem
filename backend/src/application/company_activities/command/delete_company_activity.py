from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class DeleteCompanyActivityCommand:
    company_activity_id: UUID
