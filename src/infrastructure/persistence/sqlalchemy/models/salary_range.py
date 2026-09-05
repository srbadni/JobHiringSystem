from uuid import UUID, uuid4
from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.persistence.sqlalchemy.base import Base

if TYPE_CHECKING:
    from .job_posting import JobPosting
    from .job_preference import JobPreference


class SalaryRange(Base):
    __tablename__ = "salary_ranges"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, init=False, default_factory=uuid4)
    title: Mapped[str] = mapped_column(String, nullable=False)
    min_salary: Mapped[int | None] = mapped_column(Integer, default=None)
    max_salary: Mapped[int | None] = mapped_column(Integer, default=None)

    job_postings: Mapped[list["JobPosting"]] = relationship("JobPosting", back_populates="salary_range", init=False)
    job_preferences: Mapped[list["JobPreference"]] = relationship("JobPreference", back_populates="minimum_salary_range", init=False)
