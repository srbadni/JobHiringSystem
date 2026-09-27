from dataclasses import dataclass


@dataclass
class EmployerLoginCommand:
    email: str
    password: str