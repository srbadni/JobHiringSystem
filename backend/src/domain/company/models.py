from dataclasses import dataclass, field
from uuid import UUID, uuid4

from .enums import EmployeeCount


@dataclass(slots=True)
class Company:
    name: str
    persian_name: str
    phone_number: str
    province_id: UUID
    city_id: UUID
    activity_id: UUID
    personnel_count: EmployeeCount
    id: UUID = field(default_factory=uuid4)
    logo_path: str | None = None
    description: str | None = None
    website: str | None = None
