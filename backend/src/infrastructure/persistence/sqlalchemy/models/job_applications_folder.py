from uuid import UUID, uuid4
from typing import TYPE_CHECKING

from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.persistence.sqlalchemy.base import Base

if TYPE_CHECKING:
    from .job_application import JobApplication


class JobApplicationsFolder(Base):
    __tablename__ = "job_applications_folder"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, init=False, default_factory=uuid4)
    title: Mapped[str] = mapped_column(String(120), nullable=False)

    job_applications: Mapped[list["JobApplication"]] = relationship("JobApplication", back_populates="folder", init=False)
