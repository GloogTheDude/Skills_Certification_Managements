from services.login_service import LoginService

class LoginController:

    def __init__(self, login_service: LoginService):
        self.login_service = login_service

    def login(self, mail: str, password: str) -> tuple[bool, object | None, str | None]:
        employee = self.login_service.login(mail, password)

        if employee is None:
            return False, None, "Invalid credentials"

        role = employee.role.denomination_role

        if role == "Employee":
            return True, employee, "employee_dashboard"

        if role == "Team Lead":
            return True, employee, "manager_dashboard"

        if role == "HR":
            return True, employee, "hr_dashboard"

        return True, employee, "default_dashboard"