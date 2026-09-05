from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import String, Uuid, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from domain.user.enums import UserType
from infrastructure.persistence.sqlalchemy.base import Base

if TYPE_CHECKING:
    from .applicant_profile import ApplicantProfile
    from .company_membership import CompanyMembership
    from .job_application import JobApplication


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)

    full_name: Mapped[str] = mapped_column(
        String(90),
    )

    phone_number: Mapped[str] = mapped_column(
        String(11),
    )

    email: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True,
    )

    hashed_password: Mapped[str] = mapped_column(
        String(100),
    )

    profile_image_url: Mapped[str | None] = mapped_column(
        String,
        default=None
    )

    is_superuser: Mapped[bool] = mapped_column(
        default=False,
    )

    user_type: Mapped[UserType] = mapped_column(
        Enum(
            UserType,
            values_callable=lambda enum: [item.value for item in enum]
        ),
        default=UserType.APPLICANT,
    )

    email_verified: Mapped[bool] = mapped_column(
        default=False,
    )

    applicant_profile: Mapped["ApplicantProfile | None"] = relationship(
        "ApplicantProfile",
        back_populates="applicant",
        init=False,
        uselist=False,
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    company_membership: Mapped["CompanyMembership | None"] = relationship(
        "CompanyMembership",
        back_populates="user",
        init=False,
        uselist=False,
    )

    job_applications: Mapped[list["JobApplication"]] = relationship(
        "JobApplication",
        back_populates="applicant",
        init=False,
        passive_deletes=True,
        cascade="all, delete-orphan",
    )
