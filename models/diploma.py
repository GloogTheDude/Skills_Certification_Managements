from sqlalchemy import ForeignKey, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Diploma(Base):
    __tablename__ = "diploma"

    id_diploma: Mapped[int] = mapped_column(primary_key=True)
    subject_diploma: Mapped[str | None] = mapped_column(String(50))
    level_diploma: Mapped[str | None] = mapped_column(String(50))
    is_deleted: Mapped[bool] = mapped_column(
                                            Boolean,
                                            default=False,
                                            server_default="false",
                                            nullable=False
                                        )

    id_domaine: Mapped[int] = mapped_column(ForeignKey("domaine.id_domaine"))

    domaine = relationship("Domaine", back_populates="diplomas")
    employees = relationship("EmployeeDiploma", back_populates="diploma")
    skill_links = relationship("DiplomaSkill", back_populates="diploma")
    training_links = relationship("TrainingDiploma", back_populates="diploma")
