from models.employee import Employee
from menus.employee_menu import EmployeeMenu
from services.skill_service import SkillService
from services.certification_service import CertificationService
from services.training_service import TrainingService
from db.repositories.training_repository import TrainingRepository
from services.training_request_service import TrainingRequestService
from dto.employee_dto import EmployeeDTO
from menus.manager_menu import ManagerMenu
from menus.validation_request_menu import ValidationRequestMenu
from core.constants import TRAININGREQUESTSTATUS
from controllers.training_request_controller import TrainingRequestController
class ManagerController():
    def __init__(self,manager: EmployeeDTO,
                 skill_service: SkillService, 
                 certification_service:CertificationService,
                 training_service: TrainingService,
                 training_request_service: TrainingRequestService):
        self.manager = manager
        self.skill_service = skill_service
        self.certification_service=certification_service
        self.training_service = training_service
        self.training_request_service = training_request_service
        self.training_request_controller = TrainingRequestController(self.manager)

    def get_main_manager_menu(self):
        em = EmployeeMenu()
        mm = ManagerMenu()
        user_choice = -1
        while user_choice != 0:
            user_choice = mm.main_menu()
            match user_choice:
                case 1: #1. see skills
                    skills= self.skill_service.get_skill_employee(self.manager.id_employee)
                    em.display_skills(skills_employee=skills)
                case 2: 
                    certifications_employee = self.certification_service.fetch_certification_employee(self.manager.id_employee)
                    em.display_certification(certifications_employee)
                case 3: #3. ask for training
                    self.training_request_controller.get_training_request_menu()
                case 4:
                    self.training_request_controller.follow_up_request()
                case 5:
                    #subordonate request to (in)validate
                    print("choice 5!")
                    self.training_request_controller.manage_pending_requests_for_manager(self.manager)
                case 0:
                    return 
                
    
