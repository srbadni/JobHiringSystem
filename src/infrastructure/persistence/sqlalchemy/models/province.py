from uuid import UUID, uuid4
from typing import TYPE_CHECKING

from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.persistence.sqlalchemy.base import Base

if TYPE_CHECKING:
    from .city import City
    from .company import Company
    from .job_posting import JobPosting


class Province(Base):
    __tablename__ = "provinces"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, init=False, default_factory=uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    english_name: Mapped[str] = mapped_column(String, nullable=False)

    cities: Mapped[list["City"]] = relationship("City", init=False, back_populates="province")
    job_postings: Mapped[list["JobPosting"]] = relationship("JobPosting", init=False, back_populates="province")
    companies: Mapped[list["Company"]] = relationship("Company", init=False, back_populates="province")
