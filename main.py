from core.database import SessionLocal
from db.repositories.employee_repository import EmployeeRepository
from services.login_service import LoginService


def main():
    mail = input("Mail: ")
    password = input("Password: ")

    with SessionLocal() as session:
        employee_repo = EmployeeRepository(session)
        login_service = LoginService(employee_repo)

        employee = login_service.login(mail, password)

        if employee is None:
            print("Login failed")
            return

        print(
            f"Welcome {employee.first_name} {employee.last_name} "
            f"({employee.role.denomination_role})"
        )


if __name__ == "__main__":
    main()