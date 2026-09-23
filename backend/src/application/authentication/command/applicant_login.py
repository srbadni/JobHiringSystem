from dataclasses import dataclass


@dataclass
class ApplicantLoginCommand:
    email: str
    password: str