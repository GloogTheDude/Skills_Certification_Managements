from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class TrainingSkill(Base):
    __tablename__ = "trainingxskill"

    id_skill: Mapped[int] = mapped_column(ForeignKey("skill.id_skill"), primary_key=True)
    id_training: Mapped[int] = mapped_column(ForeignKey("training.id_training"), primary_key=True)
    granted_level: Mapped[int | None]

    skill = relationship("Skill", back_populates="training_links")
    training = relationship("Training", back_populates="skill_links")
