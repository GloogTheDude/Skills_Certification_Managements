from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class AccessLevel(Base):
    __tablename__ = "access_level"

    id_access_level: Mapped[int] = mapped_column(primary_key=True)
    label: Mapped[str] = mapped_column(String(50), nullable=False)
    level: Mapped[int] = mapped_column(nullable=False)