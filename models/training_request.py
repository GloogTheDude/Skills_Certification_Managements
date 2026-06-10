from datetime import date

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class TrainingRequest(Base):
    __tablename__ = "training_request"

    id_training_request: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str | None] = mapped_column(String(50))
    reason: Mapped[str | None] = mapped_column(String(50))
    requested_at: Mapped[date | None] = mapped_column(Date)

    id_employee: Mapped[int] = mapped_column(ForeignKey("employee.id_employee"))
    id_training: Mapped[int | None] = mapped_column(ForeignKey("training.id_training"))
    id_validator: Mapped[int] = mapped_column(ForeignKey("employee.id_employee"))

    employee = relationship(
        "Employee",
        foreign_keys=[id_employee],
        back_populates="training_requests",
    )
    training = relationship("Training", back_populates="requests")
    validator = relationship(
        "Employee",
        foreign_keys=[id_validator],
        back_populates="training_requests_validated",
    )
