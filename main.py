from core.database import SessionLocal
from db.repositories.employee_repository import EmployeeRepository
from services.login_service import LoginService
from controllers.login_controller import LoginController
from controllers.employee_controller import EmployeeController
from db.repositories.skills_repository import SkillRepository
from services.skill_service import SkillService
from services.certification_service import CertificationService
from db.repositories.certification_repository import CertificationRepository
from services.training_service import TrainingService
from db.repositories.training_repository import TrainingRepository
from services.training_request_service import TrainingRequestService
from db.repositories.training_request_repository import TrainingRequestRepository
from dto.employee_dto import EmployeeDTO
from controllers.manager_controller import ManagerController


def main():
    

    mail = input("Mail: ")
    password = input("Password: ")

    with SessionLocal() as session:
        employee_repo = EmployeeRepository(session)
        login_serv = LoginService(employee_repo)
        login_control = LoginController(login_serv)
        succes,employee_dto,extra = login_control.login(mail, password)
    
    if succes:
        print(f"access_label = {employee_dto.access_label}")
        role = employee_dto.access_label
        if role == "Employee":
            employee_controller = EmployeeController(employee_dto)
            employee_controller.get_main_employee_menu()
        elif role == "Manager":
            manager_controller = ManagerController(employee_dto)
            manager_controller.get_main_manager_menu()
        elif role == "HR":
            print("HR menu under-construction")
    else:
        print("not a valid login/password")


if __name__ == "__main__":
    main()