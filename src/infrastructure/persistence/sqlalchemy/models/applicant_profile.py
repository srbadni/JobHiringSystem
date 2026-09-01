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
    from .media import Media
    from .user import User


class ApplicantProfile(Base):
    __tablename__ = "applicant_profiles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, init=False)
    applicant_id: Mapped[UUID] = mapped_column(
        Uuid,
        ForeignKey("users.id", ondelete="CASCADE",),
        nullable=False,
        unique=True,
    )
    attached_resume_id: Mapped[int | None] = mapped_column(
        Integer,
        ForeignKey("media.id", ondelete="SET NULL"),
        nullable=True,
        unique=True,
        init=False,
    )

    specialization: Mapped[str | None] = mapped_column(String(100), init=False)
    birth_year: Mapped[int | None] = mapped_column(Integer, init=False)
    gender: Mapped[Gender | None] = mapped_column(String(20), init=False)
    military_status: Mapped[MilitaryServiceStatus | None] = mapped_column(String(50), init=False)
    martial_status: Mapped[MartialStatus | None] = mapped_column(String(20), init=False)
    province: Mapped[str | None] = mapped_column(String(50), init=False)
    address: Mapped[str | None] = mapped_column(Text, init=False)
    about: Mapped[str | None] = mapped_column(Text, init=False)

    applicant: Mapped["User"] = relationship(
        "User",
        back_populates="applicant_profile",
        init=False
    )
    attached_resume: Mapped["Media | None"] = relationship(
        "Media",
        back_populates="attached_resume_profile",
        foreign_keys=[attached_resume_id],
        uselist=False,
        init=False,
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
