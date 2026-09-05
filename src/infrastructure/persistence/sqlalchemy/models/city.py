from uuid import UUID, uuid4
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.persistence.sqlalchemy.base import Base

if TYPE_CHECKING:
    from .company import Company
    from .job_posting import JobPosting
    from .province import Province


class City(Base):
    __tablename__ = "cities"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, init=False, default_factory=uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    english_name: Mapped[str] = mapped_column(String, nullable=False)

    province_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("provinces.id"))
    province: Mapped["Province"] = relationship("Province", back_populates="cities", init=False)
    job_postings: Mapped[list["JobPosting"]] = relationship("JobPosting", init=False, back_populates="city")
    companies: Mapped[list["Company"]] = relationship("Company", init=False, back_populates="city")
