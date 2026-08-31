from typing import TYPE_CHECKING

from sqlalchemy import Integer, ForeignKey, String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from domain.applicant_language.enums import LanguageLevel
from infrastructure.persistence.sqlalchemy.base import Base

if TYPE_CHECKING:
    from .applicant_profile import ApplicantProfile


class LanguageSkill(Base):
    __tablename__ = "language_skills"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, init=False)

    profile_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("applicant_profiles.id", ondelete="CASCADE",)
    )

    language_name: Mapped[str] = mapped_column(String(100))

    level: Mapped[LanguageLevel] = mapped_column(
        Enum(LanguageLevel),
        nullable=False
    )

    applicant: Mapped["ApplicantProfile"] = relationship(
        "ApplicantProfile",
        back_populates="language_skills",
        init=False
    )