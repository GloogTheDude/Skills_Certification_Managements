
from core.database import SessionLocal
from db.repositories.search_employee_skills_repository import SearchEmployeeSkillRepository
from services.search_employee_skills_service import SearchEmployeeSkillsService
from menus.search_employee_skills_menu import SearchEmployeeSkillsMenu as sesm


class SearchEmployeeSkillsController:
    def __init__(self):
        self.filter = {}
        self.employees = {}
    
    def set_employees(self):
        with SessionLocal() as session:
            repo = SearchEmployeeSkillRepository(session)
            service = SearchEmployeeSkillsService(repo)
            self.employees = service.fetch_employee_skills()
    

