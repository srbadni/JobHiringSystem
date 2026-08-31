from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.persistence.sqlalchemy.base import Base

if TYPE_CHECKING:
    from .job_posting import JobPosting


class JobCategory(Base):
    __tablename__ = "job_categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, init=False)
    code: Mapped[str] = mapped_column(String, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)

    job_postings: Mapped[list["JobPosting"]] = relationship("JobPosting", back_populates="job_category")
