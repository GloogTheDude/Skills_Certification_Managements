from sqlalchemy import select, func
from sqlalchemy.orm import Session

from models.employee import Employee
from models.role import Role
from models.skill import Skill
from models.skill_validation import SkillValidation

class SkillRepository():
    def __init__(self, session: Session):
        self.session = session
    
    def get_by_id(self, skill_id:int)-> Skill:
        return self.session.get( Skill, skill_id)

    def get_employee_skills(self, employee_id)->list[tuple[Skill, int]]:
        stmt = (
            select(
                Skill,
                SkillValidation.level_skill
            )
            .outerjoin(
                SkillValidation,
                Skill.id_skill == SkillValidation.id_skill
            )
            .where(
                SkillValidation.id_employee == employee_id,
                Skill.is_deleted == False,
                SkillValidation.is_deleted == False,
            )
        )
        result = self.session.execute(stmt).all()
        return result
