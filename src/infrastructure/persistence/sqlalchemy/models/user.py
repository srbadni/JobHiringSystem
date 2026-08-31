from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from domain.user.enums import UserType
from infrastructure.persistence.sqlalchemy.base import Base

if TYPE_CHECKING:
    from .applicant_profile import ApplicantProfile
    from .company_membership import CompanyMembership
    from .job_application import JobApplication
    from .media import Media


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, init=False)

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

    profile_image_url: Mapped[str] = mapped_column(
        String,
    )

    is_superuser: Mapped[bool] = mapped_column(
        default=False,
    )

    user_type: Mapped[str] = mapped_column(
        String(20),
        default=UserType.APPLICANT.value,
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

    media_files: Mapped[list["Media"]] = relationship(
        "Media",
        back_populates="owner",
        passive_deletes=True,
        init=False,
    )
