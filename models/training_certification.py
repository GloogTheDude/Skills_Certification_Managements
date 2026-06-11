from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class TrainingCertification(Base):
    __tablename__ = "trainingxcertification"

    id_certification: Mapped[int] = mapped_column(
        ForeignKey("certification.id_certification"),
        primary_key=True,
    )
    id_training: Mapped[int] = mapped_column(ForeignKey("training.id_training"), primary_key=True)



    certification = relationship("Certification", back_populates="training_links")
    training = relationship("Training", back_populates="certification_links")
