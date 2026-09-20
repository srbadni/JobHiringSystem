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

    @classmethod
    def create(
            cls,
            applicant_id: UUID,
            job_posting_id: UUID,
            status: ApplicationStatus = ApplicationStatus.SENT_TO_EMPLOYER,
            folder_id: UUID | None = None,
    ) -> JobApplication:
        return cls(
            applicant_id=applicant_id,
            job_posting_id=job_posting_id,
            status=status,
            folder_id=folder_id,
        )
