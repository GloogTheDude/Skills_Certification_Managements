from db.repositories.certification_repository import CertificationRepository
from dto.employee_skill_dto import EmployeeSkillDTO
from dto.employee_certification_dto import EmployeeCertificationDTO

class CertificationService():
    def __init__(self, certification_repository:CertificationRepository):
        self.certification_repository = certification_repository
    
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