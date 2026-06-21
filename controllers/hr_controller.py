from core.database import SessionLocal
from db.repositories.acquisition_skill_repository import AcquisitionSkillRepository
from menus.employee_menu import EmployeeMenu
from db.repositories.skills_repository import SkillRepository
from services.skill_service import SkillService
from db.repositories.certification_repository import CertificationRepository
from services.certification_service import CertificationService
from dto.employee_dto import EmployeeDTO
from menus.hr_menu import HRMenu 
from controllers.training_request_controller import TrainingRequestController


class HRController():
    def __init__(self,hr: EmployeeDTO):
        self.hr = hr
        self.training_request_controller = TrainingRequestController(self.hr)

    def get_main_hr_menu(self):
        em = EmployeeMenu()
        hrm = HRMenu()
        user_choice = -1
        while user_choice != 0:
            user_choice = hrm.main_menu()
            match user_choice:
                case 1: #1. see skills
                    with SessionLocal() as session:
                        repo = SkillRepository(session)
                        acquisitionRepo = AcquisitionSkillRepository(session)
                        service = SkillService(repo, acquisitionRepo)
                        skills= acquisitionRepo.get_trainingskills_by_id_employee(self.hr.id_employee)
                    em.display_skills(skills_employee=skills)
                case 2: 
                    with SessionLocal() as session:
                        repo = CertificationRepository(session)
                        service = CertificationService(repo)
                        certifications_employee = service.fetch_certification_employee(self.hr.id_employee)
                    em.display_certification(certifications_employee)
                case 3: #3. ask for training
                    self.training_request_controller.get_training_request_menu()
                case 4:
                    self.training_request_controller.follow_up_request()
                case 5:
                    #need to change to manage_pending_requests_for_hr
                    #subordonate request to (in)validate
                    self.training_request_controller.manage_pending_requests_for_hr(self.hr)
                case 6:
                    #check certification dead or near end of life
                    pass
                case 7:
                    #crud menu
                    pass
                case 0:
                    return 
                
    
