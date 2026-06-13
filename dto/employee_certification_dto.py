from datetime import date
from dataclasses import dataclass
from dto.employee_skill_dto import EmployeeSkillDTO

@dataclass
class EmployeeCertificationDTO:
    certification_name: str
    start_date: date
    end_date: date
    expiration_date: date
    skills: list[EmployeeSkillDTO]