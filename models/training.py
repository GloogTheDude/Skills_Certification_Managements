from datetime import date

from sqlalchemy import Date, ForeignKey, String,Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Training(Base):
    __tablename__ = "training"

    id_training: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str | None] = mapped_column(String(50))

    id_domaine: Mapped[int | None] = mapped_column(ForeignKey("domaine.id_domaine"))

    start_: Mapped[date | None] = mapped_column(Date)
    end_: Mapped[date | None] = mapped_column(Date)

    is_deleted: Mapped[bool] = mapped_column(
                                            Boolean,
                                            default=False,
                                            server_default="false",
                                            nullable=False
                                        )

    domaine = relationship("Domaine", back_populates="trainings")
    requests = relationship("TrainingRequest", back_populates="training")
    participations = relationship("Participation", back_populates="training")
    diploma_links = relationship("TrainingDiploma", back_populates="training")
    skill_links = relationship("TrainingSkill", back_populates="training")
    certification_links = relationship("TrainingCertification", back_populates="training")
    providers = relationship("Provide", back_populates="training")
