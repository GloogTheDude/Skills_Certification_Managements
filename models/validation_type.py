from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class ValidationType(Base):
    __tablename__ = "validation_type"

    id_validation: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str | None] = mapped_column(String(50))
    denomination_validation: Mapped[str | None] = mapped_column(String(50))
    is_deleted: Mapped[bool] = mapped_column(
                                        Boolean,
                                        default=False,
                                        server_default="false",
                                        nullable=False
                                    )

    skill_validations = relationship("SkillValidation", back_populates="validation_type")
