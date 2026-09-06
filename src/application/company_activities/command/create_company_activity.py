from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CreateCompanyActivityCommand:
    code: str
    title: str
