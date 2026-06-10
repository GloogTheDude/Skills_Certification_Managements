from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class TrainingDiploma(Base):
    __tablename__ = "trainingxdiploma"

    id_diploma: Mapped[int] = mapped_column(ForeignKey("diploma.id_diploma"), primary_key=True)
    id_training: Mapped[int] = mapped_column(ForeignKey("training.id_training"), primary_key=True)

    diploma = relationship("Diploma", back_populates="training_links")
    training = relationship("Training", back_populates="diploma_links")
