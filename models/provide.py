from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Provide(Base):
    __tablename__ = "provide"

    id_training: Mapped[int] = mapped_column(ForeignKey("training.id_training"), primary_key=True)
    id_source: Mapped[int] = mapped_column(ForeignKey("training_source.id_source"), primary_key=True)

    cost_hour: Mapped[Decimal | None] = mapped_column(Numeric(15, 2))
    duration_hours: Mapped[Decimal | None] = mapped_column(Numeric(15, 2))

    training = relationship("Training", back_populates="providers")
    source = relationship("TrainingSource", back_populates="provided_trainings")
