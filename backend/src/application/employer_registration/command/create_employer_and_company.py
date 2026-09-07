from dataclasses import dataclass

from ...companies.command.create_company import CreateCompanyCommand
from ...users.command.create_user import CreateUserCommand


@dataclass
class CreateEmployerAndCompany:
    employer: CreateUserCommand
    company: CreateCompanyCommand