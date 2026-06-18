from sqlalchemy import ForeignKey,Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class DiplomaSkill(Base):
    __tablename__ = "diplomaxskill"

    id_diploma: Mapped[int] = mapped_column(ForeignKey("diploma.id_diploma"), primary_key=True)
    id_skill: Mapped[int] = mapped_column(ForeignKey("skill.id_skill"), primary_key=True)
    min_level: Mapped[int | None]
    is_deleted: Mapped[bool] = mapped_column(
                                            Boolean,
                                            default=False,
                                            server_default="false",
                                            nullable=False
                                        )

    diploma = relationship("Diploma", back_populates="skill_links")
    skill = relationship("Skill", back_populates="diploma_links")