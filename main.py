from core.database import SessionLocal
from db.repositories.employee_repository import EmployeeRepository
from services.login_service import LoginService
from controllers.login_controller import LoginController
from controllers.employee_controller import EmployeeController
from db.repositories.skills_repository import SkillRepository
from services.skill_service import SkillService


def main():
    session = SessionLocal()
    employee_repo = EmployeeRepository(session)
    login_serv = LoginService(employee_repo)
    login_control = LoginController(login_serv)
    skill_repo = SkillRepository(session)
    skill_service = SkillService(skill_repo)

    
    mail = input("Mail: ")
    password = input("Password: ")
    
    succes,employee,extra = login_control.login(mail, password)
    
    if succes:
        role = employee.role.denomination_role 
        if role == "Employee":
            #print("employee menu under-construction")
            employee_controller = EmployeeController(employee,skill_service)
            employee_controller.get_main_employee_menu()
        elif role == "Manager":
            print("manager menu under-construction")
        elif role == "HR":
            print("HR menu under-construction")
    else:
        print("not a valid login/password")


if __name__ == "__main__":
    main()