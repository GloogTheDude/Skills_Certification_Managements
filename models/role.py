from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Role(Base):
    __tablename__ = "role"

    id_role: Mapped[int] = mapped_column(primary_key=True)

    denomination_role: Mapped[str | None] = mapped_column(String(50))

    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        server_default="false",
        nullable=False,
    )

    id_access_level: Mapped[int] = mapped_column(
        ForeignKey("access_level.id_access_level"),
        nullable=False,
        default=1,
        server_default="1",
    )

    employees = relationship("Employee", back_populates="role")
    access_level = relationship("AccessLevel")