from sqlalchemy import ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class CertificationSkill(Base):
    __tablename__ = "certificationxskill"

    id_certification: Mapped[int] = mapped_column(
        ForeignKey("certification.id_certification"),
        primary_key=True,
    )
    id_skill: Mapped[int] = mapped_column(ForeignKey("skill.id_skill"), primary_key=True)
    granted_level: Mapped[int | None]
    is_deleted: Mapped[bool] = mapped_column(
                                        Boolean,
                                        default=False,
                                        server_default="false",
                                        nullable=False
                                    )
    certification = relationship("Certification", back_populates="skill_links")
    skill = relationship("Skill", back_populates="certification_links")
    trainings = relationship("Training", back_populates="certification")
