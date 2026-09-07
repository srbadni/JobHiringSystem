from typing import Annotated
from uuid import UUID
from fastapi import Header

# Development-only identity selectors. These do not provide authentication or
# authorization and must be replaced by claims from the authenticated principal.
SelectedCompanyId = Annotated[UUID, Header(alias="X-Company-Id")]
SelectedApplicantId = Annotated[UUID, Header(alias="X-Applicant-Id")]
