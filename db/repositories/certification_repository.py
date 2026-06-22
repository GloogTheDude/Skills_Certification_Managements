from sqlalchemy import select, func, or_
from sqlalchemy.orm import Session


from models.domaine import Domaine
from models.employee_certification import EmployeeCertification
from models.certification import Certification 
from models.certification_skill import CertificationSkill
from models.skill import Skill
from models.employee import Employee

class CertificationRepository():
    def __init__(self, session: Session):
        self.session = session
    

    def get_certification_skill_by_id_employee(self, id_employee: int):
        stmt = (
            select(
                EmployeeCertification,
                Certification,
                CertificationSkill.granted_level,
                Skill.name_skill,
            )
            .join(
                Certification,
                EmployeeCertification.id_certification == Certification.id_certification,
            )
            .outerjoin(
                CertificationSkill,
                Certification.id_certification == CertificationSkill.id_certification,
            )
            .outerjoin(
                Skill,
                CertificationSkill.id_skill == Skill.id_skill,
            )
            .where(
                EmployeeCertification.id_employee == id_employee,
                EmployeeCertification.is_deleted.is_(False),
                Certification.is_deleted.is_(False),
                or_(
                    CertificationSkill.id_skill.is_(None),
                    CertificationSkill.is_deleted.is_(False),
                ),
                or_(
                    Skill.id_skill.is_(None),
                    Skill.is_deleted.is_(False),
                ),
            )
        )
        return self.session.execute(stmt).all()

    def get_all(self) -> list[Certification]:
        stmt = (
            select(Certification)
            .where(Certification.is_deleted.is_(False))
            .order_by(Certification.id_certification)
        )
        return self.session.scalars(stmt).all()

    def get_all_for_crud(self):
        stmt = (
            select(
                Certification.id_certification,
                Certification.subject_certification,
                Certification.validity_month,
                Certification.id_domaine,
                Domaine.nom_domaine,
            )
            .outerjoin(Domaine, Domaine.id_domaine == Certification.id_domaine)
            .where(Certification.is_deleted.is_(False))
            .order_by(Certification.id_certification)
        )
        return self.session.execute(stmt).all()

    def get_by_id(self, id_certification: int) -> Certification | None:
        return self.session.get(Certification, id_certification)

    def add(self, certification: Certification) -> Certification:
        self.session.add(certification)
        return certification

    def soft_delete(self, certification: Certification) -> None:
        certification.is_deleted = True

        