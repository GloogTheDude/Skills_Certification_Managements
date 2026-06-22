from dto.employee_dto import EmployeeCrudDTO


class EmployeeCrudMenu:
    @staticmethod
    def main_menu() -> int:
        user_choice = -1

        while not (0 <= user_choice <= 4):
            print("===== EMPLOYEE CRUD =====")
            print("1. List employees")
            print("2. Create employee")
            print("3. Update employee")
            print("4. Delete employee")
            print("0. Leave")

            user_choice = int(input("Your choice: "))

        return user_choice

    @staticmethod
    def display_employees(employees: list[EmployeeCrudDTO]) -> None:
        print("===== EMPLOYEES =====")

        if not employees:
            print("No employee found.")
            return

        for employee in employees:
            manager = employee.manager_name or "No manager"

            print(
                f"{employee.id_employee}: "
                f"{employee.first_name} {employee.last_name} | "
                f"{employee.mail} | "
                f"Role: {employee.role_name} | "
                f"Manager: {manager}"
            )

    @staticmethod
    def ask_id_employee() -> int:
        return int(input("Employee id: "))

    @staticmethod
    def ask_first_name() -> str:
        return input("First name: ").strip()

    @staticmethod
    def ask_last_name() -> str:
        return input("Last name: ").strip()

    @staticmethod
    def ask_mail() -> str:
        return input("Mail: ").strip()

    @staticmethod
    def ask_password() -> str:
        return input("Password/hash: ").strip()

    @staticmethod
    def ask_optional_password() -> str | None:
        raw_value = input("Password/hash, empty to keep current: ").strip()

        if raw_value == "":
            return None

        return raw_value

    @staticmethod
    def ask_id_role() -> int:
        return int(input("Role id: "))

    @staticmethod
    def ask_id_manager() -> int | None:
        raw_value = input("Manager id, empty if none: ").strip()

        if raw_value == "":
            return None

        return int(raw_value)

    @staticmethod
    def display_success(message: str) -> None:
        print(message)

    @staticmethod
    def display_error(message: str) -> None:
        print(message)