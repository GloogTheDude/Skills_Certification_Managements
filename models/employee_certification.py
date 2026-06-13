from datetime import date

from sqlalchemy import Boolean, Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class EmployeeCertification(Base):
    __tablename__ = "employeexcertification"

    id_employee_certification: Mapped[int] = mapped_column(
        primary_key=True
    )

    id_employee: Mapped[int] = mapped_column(
        ForeignKey("employee.id_employee")
    )

    id_certification: Mapped[int] = mapped_column(
        ForeignKey("certification.id_certification")
    )

    start_: Mapped[date | None] = mapped_column(Date)
    end_: Mapped[date | None] = mapped_column(Date)
    expiration: Mapped[date | None] = mapped_column(Date)

    organism: Mapped[str | None] = mapped_column(String(50))
    evaluation: Mapped[str | None] = mapped_column(String(50))
    doc: Mapped[str | None] = mapped_column(String(255))

    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        server_default="false",
        nullable=False,
    )

    employee = relationship(
        "Employee",
        back_populates="certifications"
    )

    certification = relationship(
        "Certification",
        back_populates="employees"
    )