from db.repositories.certification_repository import CertificationRepository
from db.repositories.domaine_repository import DomaineRepository
from dto.certification_dto import CertificationCrudDTO
from dto.employee_skill_dto import EmployeeSkillDTO
from dto.employee_certification_dto import EmployeeCertificationDTO
from models.certification import Certification

class CertificationService():
    def __init__(self,certification_repository: CertificationRepository,
        domaine_repository: DomaineRepository | None = None,):
        self.certification_repository = certification_repository
        self.domaine_repository = domaine_repository

    def fetch_certification_employee(self, id_employee: int) -> list[EmployeeCertificationDTO]:
        rows = self.certification_repository.get_certification_skill_by_id_employee(id_employee)

        certifications: dict[int, EmployeeCertificationDTO] = {}

        for emp_cert, cert, level, skill_name in rows:
            emp_cert_id = emp_cert.id_employee_certification

            if emp_cert_id not in certifications:
                certifications[emp_cert_id] = EmployeeCertificationDTO(
                    certification_name=cert.subject_certification,
                    start_date=emp_cert.start_,
                    end_date=emp_cert.end_,
                    expiration_date=emp_cert.expiration,
                    skills=[],
                )

            if skill_name is not None:
                certifications[emp_cert_id].skills.append(
                    EmployeeSkillDTO(
                        skill_name=skill_name,
                        level=level,
                    )
                )

        return list(certifications.values())

    def get_all(self) -> list[Certification]:
        return self.certification_repository.get_all()

    def get_all_for_crud(self) -> list[CertificationCrudDTO]:
        rows = self.certification_repository.get_all_for_crud()

        return [
            CertificationCrudDTO(
                id_certification=id_certification,
                subject_certification=subject_certification,
                validity_month=validity_month,
                id_domaine=id_domaine,
                domaine_name=domaine_name,
            )
            for (
                id_certification,
                subject_certification,
                validity_month,
                id_domaine,
                domaine_name,
            ) in rows
        ]

    def get_by_id(self, id_certification: int) -> Certification | None:
        return self.certification_repository.get_by_id(id_certification)

    def create(
        self,
        subject_certification: str,
        validity_month: int | None,
        id_domaine: int,
    ) -> Certification | None:
        if self.domaine_repository is not None:
            domaine = self.domaine_repository.get_by_id(id_domaine)

            if domaine is None or domaine.is_deleted:
                return None

        certification = Certification()
        certification.subject_certification = subject_certification
        certification.validity_month = validity_month
        certification.id_domaine = id_domaine
        certification.is_deleted = False

        return self.certification_repository.add(certification)

    def update(
        self,
        id_certification: int,
        subject_certification: str,
        validity_month: int | None,
        id_domaine: int,
    ) -> Certification | None:
        certification = self.certification_repository.get_by_id(id_certification)

        if certification is None or certification.is_deleted:
            return None

        if self.domaine_repository is not None:
            domaine = self.domaine_repository.get_by_id(id_domaine)

            if domaine is None or domaine.is_deleted:
                return None

        certification.subject_certification = subject_certification
        certification.validity_month = validity_month
        certification.id_domaine = id_domaine

        return certification

    def delete(self, id_certification: int) -> bool:
        certification = self.certification_repository.get_by_id(id_certification)

        if certification is None or certification.is_deleted:
            return False

        self.certification_repository.soft_delete(certification)
        return True