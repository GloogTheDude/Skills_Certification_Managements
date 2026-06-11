from sqlalchemy import ForeignKey, String,Date, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from datetime import date

class EmployeeDiploma(Base):
    __tablename__ = "employeexdiploma"

    id_employee: Mapped[int] = mapped_column(ForeignKey("employee.id_employee"), primary_key=True)
    id_diploma: Mapped[int] = mapped_column(ForeignKey("diploma.id_diploma"), primary_key=True)

    end_: Mapped[date | None] = mapped_column(Date)

    school: Mapped[str | None] = mapped_column(String(50))
    
    start_: Mapped[date | None] = mapped_column(Date)
    
    distinction: Mapped[str | None] = mapped_column(String(50))
    doc: Mapped[str | None] = mapped_column(String(50))

    is_deleted: Mapped[bool] = mapped_column(
                                            Boolean,
                                            default=False,
                                            server_default="false",
                                            nullable=False
                                        )

    employee = relationship("Employee", back_populates="diplomas")
    diploma = relationship("Diploma", back_populates="employees")
