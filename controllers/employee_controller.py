from core.database import SessionLocal
from models.employee import Employee
from menus.employee_menu import EmployeeMenu
from dto.employee_skill_dto import EmployeeSkillDTO
from db.repositories.skills_repository import SkillRepository
from services.skill_service import SkillService

class EmployeeController():
    def __init__(self,emp: Employee,skill_service: SkillService):
        self.employee = emp
        self.skill_service = skill_service
    
    def get_main_employee_menu(self):
        em = EmployeeMenu()
        user_choice = -1
        while user_choice != 0:
            user_choice = em.main_menu()
            match user_choice:
                case 1: #1. see skills
                    skills= self.skill_service.get_skill_employee(self.employee.id_employee)
                    em.display_skills(skills_employee=skills)
                case 2: #2. see certifications
                    pass
                case 3: #3. ask for training
                    pass
                case 0:
                    return 