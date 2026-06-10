from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Participation(Base):
    __tablename__ = "participation"

    id_employee: Mapped[int] = mapped_column(ForeignKey("employee.id_employee"), primary_key=True)
    id_training: Mapped[int] = mapped_column(ForeignKey("training.id_training"), primary_key=True)

    status: Mapped[str] = mapped_column(String(50))

    employee = relationship("Employee", back_populates="participations")
    training = relationship("Training", back_populates="participations")
