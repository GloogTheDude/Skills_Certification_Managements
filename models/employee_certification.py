from sqlalchemy import ForeignKey, String, Date, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from datetime import date

class EmployeeCertification(Base):
    __tablename__ = "employeexcertification"

    id_employee: Mapped[int] = mapped_column(ForeignKey("employee.id_employee"), primary_key=True)
    id_certification: Mapped[int] = mapped_column(ForeignKey("certification.id_certification"), primary_key=True)

    start_: Mapped[date | None] = mapped_column(Date)
    end_: Mapped[date | None] = mapped_column(Date)
    expiration: Mapped[date | None] = mapped_column(Date)
    
    organism: Mapped[str | None] = mapped_column(String(50))
    evaluation: Mapped[str | None] = mapped_column(String(50))
    doc: Mapped[str | None] = mapped_column(String(50))

    is_deleted: Mapped[bool] = mapped_column(
                                        Boolean,
                                        default=False,
                                        server_default="false",
                                        nullable=False
                                    )

    employee = relationship("Employee", back_populates="certifications")
    certification = relationship("Certification", back_populates="employees")
