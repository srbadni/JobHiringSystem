from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.persistence.sqlalchemy.base import Base

if TYPE_CHECKING:
    from .user import User
    from .job_posting import JobPosting
    from .job_applications_folder import JobApplicationsFolder


class JobApplication(Base):
    __tablename__ = "job_applications"

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
    status: Mapped[str] = mapped_column(String(50), nullable=False)

    applicant: Mapped["User"] = relationship(
        "User", back_populates="job_applications", init=False
    )
    job_posting: Mapped["JobPosting"] = relationship(
        "JobPosting", back_populates="job_applications", init=False
    )
    folder: Mapped["JobApplicationsFolder | None"] = relationship(
        "JobApplicationsFolder", back_populates="job_applications", init=False
    )
