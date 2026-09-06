from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, Integer, String, Text, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from domain.applicant_profile.enum import Gender, MartialStatus
from domain.job_posting.enum import MilitaryServiceStatus
from infrastructure.persistence.sqlalchemy.base import Base

if TYPE_CHECKING:
    from .applicant_education_history import Education
    from .applicant_language import LanguageSkill
    from .applicant_skill import ApplicantSkill
    from .applicant_work_experience import WorkExperience
    from .job_preference import JobPreference
    from .user import User
    from .attached_resume import AttachedResume


class ApplicantProfile(Base):
    __tablename__ = "applicant_profiles"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    applicant_id: Mapped[UUID] = mapped_column(
        Uuid,
        ForeignKey("users.id", ondelete="CASCADE",),
        nullable=False,
        unique=True,
    )

    specialization: Mapped[str | None] = mapped_column(String(100))
    birth_year: Mapped[int | None] = mapped_column(Integer)
    gender: Mapped[Gender | None] = mapped_column(String(20))
    military_status: Mapped[MilitaryServiceStatus | None] = mapped_column(String(50))
    martial_status: Mapped[MartialStatus | None] = mapped_column(String(20))
    province: Mapped[str | None] = mapped_column(String(50))
    address: Mapped[str | None] = mapped_column(Text)
    about: Mapped[str | None] = mapped_column(Text)

    applicant: Mapped["User"] = relationship(
        "User",
        back_populates="applicant_profile",
        init=False
    )
    skills: Mapped[list["ApplicantSkill"]] = relationship(
        "ApplicantSkill",
        cascade="all, delete-orphan",
        passive_deletes=True,
        back_populates="applicant_profile",
        init=False,
    )
    work_experiences: Mapped[list["WorkExperience"]] = relationship(
        "WorkExperience",
        cascade="all, delete-orphan",
        passive_deletes=True,
        back_populates="applicant",
        init=False,
    )
    educations: Mapped[list["Education"]] = relationship(
        "Education",
        cascade="all, delete-orphan",
        passive_deletes=True,
        back_populates="applicant",
        init=False,
    )
    language_skills: Mapped[list["LanguageSkill"]] = relationship(
        "LanguageSkill",
        cascade="all, delete-orphan",
        passive_deletes=True,
        back_populates="applicant",
        init=False,
    )

    job_preference: Mapped["JobPreference | None"] = relationship(
        "JobPreference",
        back_populates="applicant",
        cascade="all, delete-orphan",
        passive_deletes=True,
        uselist=False,
        init=False,
    )

    attached_resume: Mapped["AttachedResume | None"] = relationship(
        "AttachedResume",
        back_populates="applicant_profile",
        cascade="all, delete-orphan",
        passive_deletes=True,
        uselist=False,
        init=False,
    )
