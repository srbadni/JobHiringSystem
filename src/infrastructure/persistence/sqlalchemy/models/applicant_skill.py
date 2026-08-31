from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.persistence.sqlalchemy.base import Base

if TYPE_CHECKING:
    from .applicant_profile import ApplicantProfile


class ApplicantSkill(Base):
    __tablename__ = "applicant_skills"

    __table_args__ = (
        UniqueConstraint(
            "applicant_profile_id",
            "title"
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, init=False)
    applicant_profile_id: Mapped[int] = mapped_column(Integer, ForeignKey("applicant_profiles.id", ondelete="CASCADE",))
    title: Mapped[str] = mapped_column(String(90))

    applicant_profile: Mapped["ApplicantProfile"] = relationship("ApplicantProfile", back_populates="skills", init=False)