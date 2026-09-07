from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, Uuid, Enum, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from domain.job_application.enums import ApplicationStatus
from infrastructure.persistence.sqlalchemy.base import Base

if TYPE_CHECKING:
    from .user import User
    from .job_posting import JobPosting
    from .job_applications_folder import JobApplicationsFolder


class JobApplication(Base):
    __tablename__ = "job_applications"
    __table_args__ = (
        UniqueConstraint(
            "applicant_id",
            "job_posting_id",
            name="uq_job_applications_applicant_job_posting",
        ),
    )

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, init=False, default_factory=uuid4)
    folder_id: Mapped[UUID | None] = mapped_column(
        Uuid, ForeignKey("job_applications_folder.id"), nullable=True
    )
    applicant_id: Mapped[UUID] = mapped_column(
        Uuid,
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    job_posting_id: Mapped[UUID] = mapped_column(
        Uuid, ForeignKey("job_postings.id"), nullable=False
    )
    status: Mapped[ApplicationStatus] = mapped_column(
        Enum(ApplicationStatus, name="application_status"),
        nullable=False,
    )

    applicant: Mapped["User"] = relationship(
        "User", back_populates="job_applications", init=False
    )
    job_posting: Mapped["JobPosting"] = relationship(
        "JobPosting", back_populates="job_applications", init=False
    )
    folder: Mapped["JobApplicationsFolder | None"] = relationship(
        "JobApplicationsFolder", back_populates="job_applications", init=False
    )
