from sqlalchemy import String,Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Skill(Base):
    __tablename__ = "skill"

    id_skill: Mapped[int] = mapped_column(primary_key=True)
    name_skill: Mapped[str | None] = mapped_column(String(50))
    is_deleted: Mapped[bool] = mapped_column(
                                            Boolean,
                                            default=False,
                                            server_default="false",
                                            nullable=False
                                        )

    validations = relationship("SkillValidation", back_populates="skill")
    certification_links = relationship("CertificationSkill", back_populates="skill")
    diploma_links = relationship("DiplomaSkill", back_populates="skill")
    training_links = relationship("TrainingSkill", back_populates="skill")
