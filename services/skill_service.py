from db.repositories.skills_repository import SkillRepository
from models.skill import Skill
from dto.employee_skill_dto import EmployeeSkillDTO

class SkillService():
    def __init__(self, skill_repo:SkillRepository):
        self.skill_repository = skill_repo

    def get_skill_employee(self, id_employee):
        result = self.skill_repository.get_employee_skills(id_employee)
        return [
            EmployeeSkillDTO(
                skill_name=skill.name_skill,
                level=level
            )
            for skill, level in result]