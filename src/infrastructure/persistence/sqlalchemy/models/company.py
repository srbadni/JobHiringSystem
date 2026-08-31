from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, Text, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from domain.company.enums import EmployeeCount
from infrastructure.persistence.sqlalchemy.base import Base

if TYPE_CHECKING:
    from .company_membership import CompanyMembership
    from .job_posting import JobPosting
    from .province import Province
    from .city import City
    from .company_activity import CompanyActivity


class Company(Base):
    """Persisted company profile."""

    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        init=False,
    )

    name: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )

    persian_name: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )

    province_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("provinces.id"),
        nullable=False,
    )

    city_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("cities.id"),
        nullable=False,
    )

    activity_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("company_activities.id"),
        nullable=False,
    )

    personnel_count: Mapped[EmployeeCount] = mapped_column(Enum(
        EmployeeCount,
        values_callable=lambda enum: [item.value for item in enum]
    ), nullable=False)

    logo_path: Mapped[str | None] = mapped_column(String(500), nullable=True)

    phone_number: Mapped[str] = mapped_column(String(20), nullable=False)

    description: Mapped[str | None] = mapped_column(
        Text,
        default=None,
    )

    website: Mapped[str | None] = mapped_column(
        String(2048),
        default=None,
    )

    company_memberships: Mapped[list["CompanyMembership"]] = relationship(
        "CompanyMembership",
        back_populates="company",
        init=False,
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    job_postings: Mapped[list["JobPosting"]] = relationship(
        "JobPosting",
        back_populates="company",
        init=False,
    )

    province: Mapped["Province"] = relationship(
        "Province",
        back_populates="companies",
        init=False
    )

    city: Mapped["City"] = relationship(
        "City",
        back_populates="companies",
        init=False
    )

    activity: Mapped["CompanyActivity"] = relationship(
        "CompanyActivity",
        back_populates="companies",
        init=False
    )