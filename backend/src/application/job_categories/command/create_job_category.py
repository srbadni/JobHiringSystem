from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CreateJobCategoryCommand:
    code: str
    title: str
