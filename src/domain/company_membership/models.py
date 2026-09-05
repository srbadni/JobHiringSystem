from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(slots=True)
class CompanyMembership:
    user_id: UUID
    company_id: UUID
    is_admin: bool
    id: UUID = field(default_factory=uuid4)
