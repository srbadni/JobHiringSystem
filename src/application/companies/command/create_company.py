from dataclasses import dataclass
from domain.company.enums import EmployeeCount


@dataclass
class CreateCompanyCommand:
    name: str
    persian_name: str
    phone_number: str
    province_id: int
    city_id: int
    activity_id: int
    personnel_count: EmployeeCount
    logo_path: str | None = None
    description: str | None = None
    website: str | None = None