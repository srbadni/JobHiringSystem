from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Integer, ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.persistence.sqlalchemy.base import Base

if TYPE_CHECKING:
    from .user import User
    from .job_posting import JobPosting
    from .job_applications_folder import JobApplicationsFolder


class JobApplication(Base):
    __tablename__ = "job_applications"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, init=False)
    folder_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("job_applications_folder.id"), nullable=True
    )
    applicant_id: Mapped[UUID] = mapped_column(
        Uuid,
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    job_posting_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("job_postings.id"), nullable=False
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
