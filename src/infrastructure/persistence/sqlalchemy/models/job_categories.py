from uuid import UUID, uuid4
from typing import TYPE_CHECKING

from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.persistence.sqlalchemy.base import Base

if TYPE_CHECKING:
    from .job_posting import JobPosting


class JobCategory(Base):
    __tablename__ = "job_categories"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, init=False, default_factory=uuid4)
    code: Mapped[str] = mapped_column(String, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)

    job_postings: Mapped[list["JobPosting"]] = relationship("JobPosting", back_populates="job_category", init=False)
