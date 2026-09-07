from dataclasses import dataclass


@dataclass(frozen=True)
class GetCompanyDetailsQuery:
    company_en_name: str
