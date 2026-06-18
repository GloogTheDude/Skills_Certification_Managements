from sqlalchemy import ForeignKey, String,Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Certification(Base):
    __tablename__ = "certification"

    id_certification: Mapped[int] = mapped_column(primary_key=True)
    subject_certification: Mapped[str | None] = mapped_column(String(50))
    is_deleted: Mapped[bool] = mapped_column(
                                        Boolean,
                                        default=False,
                                        server_default="false",
                                        nullable=False
                                    )

    id_domaine: Mapped[int] = mapped_column(ForeignKey("domaine.id_domaine"))

    domaine = relationship("Domaine", back_populates="certifications")
    employees = relationship("EmployeeCertification", back_populates="certification")
    skill_links = relationship("CertificationSkill", back_populates="certification")
    trainings = relationship("Training",back_populates="certification")

    #should add average duration
