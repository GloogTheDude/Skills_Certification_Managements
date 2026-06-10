from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class ValidationType(Base):
    __tablename__ = "validation_type"

    id_validation: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str | None] = mapped_column(String(50))
    denomination_validation: Mapped[str | None] = mapped_column(String(50))

    skill_validations = relationship("SkillValidation", back_populates="validation_type")
