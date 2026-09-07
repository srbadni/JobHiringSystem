from uuid import UUID, uuid4
from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey, UniqueConstraint, Uuid
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

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, init=False, default_factory=uuid4)
    applicant_profile_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("applicant_profiles.id", ondelete="CASCADE",))
    title: Mapped[str] = mapped_column(String(90))

    applicant_profile: Mapped["ApplicantProfile"] = relationship("ApplicantProfile", back_populates="skills", init=False)