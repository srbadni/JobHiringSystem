from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True)
class CompanyMembership:
    user_id: UUID
    company_id: UUID
    is_admin: bool
    id: int | None = None
