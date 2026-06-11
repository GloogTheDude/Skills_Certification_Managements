from datetime import date

from sqlalchemy import Date, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class SkillValidation(Base):
    __tablename__ = "skill_validation"

    id_skill_validation: Mapped[int] = mapped_column(primary_key=True)
    date_: Mapped[date | None] = mapped_column(Date)
    level_skill: Mapped[int | None]

    id_validation: Mapped[int] = mapped_column(ForeignKey("validation_type.id_validation"))
    id_employee: Mapped[int] = mapped_column(ForeignKey("employee.id_employee"))
    id_validator: Mapped[int] = mapped_column(ForeignKey("employee.id_employee"))
    id_skill: Mapped[int] = mapped_column(ForeignKey("skill.id_skill"))
    is_deleted: Mapped[bool] = mapped_column(
                                            Boolean,
                                            default=False,
                                            server_default="false",
                                            nullable=False
                                        )

    validation_type = relationship("ValidationType", back_populates="skill_validations")
    employee = relationship(
        "Employee",
        foreign_keys=[id_employee],
        back_populates="skill_validations_received",
    )
    validator = relationship(
        "Employee",
        foreign_keys=[id_validator],
        back_populates="skill_validations_validated",
    )
    skill = relationship("Skill", back_populates="validations")
