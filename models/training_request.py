from datetime import date

from sqlalchemy import Date, ForeignKey, String,Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base



class TrainingRequest(Base):
    __tablename__ = "training_request"

    id_training_request: Mapped[int] = mapped_column(primary_key=True)
    request_desc: Mapped[str] = mapped_column(String(150), nullable=True)


    status: Mapped[str] = mapped_column(String(50), nullable=False)
    reason: Mapped[str | None] = mapped_column(String(500), nullable=True)
    requested_at: Mapped[date] = mapped_column(Date, nullable=False)

    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        server_default="false",
        nullable=False,
    )

    id_employee: Mapped[int] = mapped_column(
        ForeignKey("employee.id_employee"),
        nullable=False,
    )

    id_training: Mapped[int | None] = mapped_column(
        ForeignKey("training.id_training"),
        nullable=True,
    )

    id_validator: Mapped[int | None] = mapped_column(
        ForeignKey("employee.id_employee"),
        nullable=True,
    )

    employee = relationship(
        "Employee",
        foreign_keys=[id_employee],
        back_populates="training_requests",
    )

    training = relationship(
        "Training",
        back_populates="requests",
    )

    validator = relationship(
        "Employee",
        foreign_keys=[id_validator],
        back_populates="training_requests_validated",
    )