from dataclasses import dataclass, field
from uuid import UUID, uuid4

from .enums import ApplicationStatus


@dataclass
class JobApplication:
    applicant_id: UUID
    job_posting_id: UUID
    status: ApplicationStatus = ApplicationStatus.SENT_TO_EMPLOYER
    folder_id: UUID | None = None
    id: UUID = field(default_factory=uuid4)
