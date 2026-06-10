from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Role(Base):
    __tablename__ = "role"

    id_role: Mapped[int] = mapped_column(primary_key=True)
    denomination_role: Mapped[str | None] = mapped_column(String(50))

    employees = relationship("Employee", back_populates="role")
