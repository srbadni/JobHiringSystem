from dataclasses import dataclass

from domain.company.enums import EmployeeCount


@dataclass(frozen=True)
class CompanyDetails:
    name: str
    english_name: str
    activity: str
    employee_count: EmployeeCount
    city: str
    province: str
