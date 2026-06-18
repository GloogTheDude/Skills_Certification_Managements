from models.employee import Employee
from menus.employee_menu import EmployeeMenu
from services.skill_service import SkillService
from services.certification_service import CertificationService
from controllers.training_request_controller import TrainingRequestController
from services.training_service import TrainingService
from db.repositories.training_repository import TrainingRepository
from services.training_request_service import TrainingRequestService
from dto.employee_dto import EmployeeDTO

class EmployeeController():
    def __init__(self,emp: EmployeeDTO,
                 skill_service: SkillService, 
                 certification_service:CertificationService,
                 training_service: TrainingService,
                 training_request_service: TrainingRequestService):
        self.employee = emp
        self.skill_service = skill_service
        self.certification_service=certification_service
        self.training_service = training_service
        self.training_request_service = training_request_service

    def get_main_employee_menu(self):
        em = EmployeeMenu()
        user_choice = -1
        while user_choice != 0:
            user_choice = em.main_menu()
            match user_choice:
                case 1: #1. see skills
                    skills= self.skill_service.get_skill_employee(self.employee.id_employee)
                    em.display_skills(skills_employee=skills)
                case 2: 
                    certifications_employee = self.certification_service.fetch_certification_employee(self.employee.id_employee)
                    em.display_certification(certifications_employee)
                case 3: #3. ask for training
                    trc = TrainingRequestController(self.employee)
                    trc.get_training_request_menu()
                case 4:
                    trc = TrainingRequestController(self.employee)
                    trc.follow_up_request()
                case 0:
                    return 