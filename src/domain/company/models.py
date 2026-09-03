from dataclasses import dataclass, field
from uuid import UUID, uuid4

from .enums import EmployeeCount


@dataclass(slots=True)
class Company:
    name: str
    persian_name: str
    phone_number: str
    province_id: int
    city_id: int
    activity_id: int
    personnel_count: EmployeeCount
    id: UUID = field(default_factory=uuid4)
    logo_path: str | None = None
    description: str | None = None
    website: str | None = None