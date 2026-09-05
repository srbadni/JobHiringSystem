from dataclasses import dataclass, field
from uuid import UUID, uuid4

from ..applicant_profile.enum import Gender, MartialStatus
from ..attached_resume.models import AttachedResume
from ..job_posting.enum import MilitaryServiceStatus

@dataclass
class ApplicantProfile:
    applicant_id: UUID
    specialization: str | None = None
    birth_year: int | None = None
    gender: Gender | None = None
    military_status: MilitaryServiceStatus | None = None
    martial_status: MartialStatus | None = None
    province: str | None = None
    address: str | None = None
    about: str | None = None
    attached_resume: AttachedResume | None = None
    id: UUID = field(default_factory=uuid4)
