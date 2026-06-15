import unittest

from services.login_service import LoginService
from models.employee import Employee


class FakeEmployeeRepository:
    def __init__(self, employees_by_mail):
        self.employees_by_mail = employees_by_mail

    def get_by_mail_with_access(self, mail: str):
        employee = self.employees_by_mail.get(mail)

        if employee is None:
            return None

        return (
            employee,
            "Developer",
            "Employee",
            1,
        )


class TestLoginService(unittest.TestCase):
    def make_employee(self, *, mail="test@company.be", password="hash", is_deleted=False):
        employee = Employee()
        employee.mail = mail
        employee.hash_password = password
        employee.is_deleted = is_deleted
        return employee

    def test_login_returns_employee_when_credentials_are_valid(self):
        employee = self.make_employee()
        service = LoginService(FakeEmployeeRepository({employee.mail: employee}))

        result = service.login("test@company.be", "hash")

        self.assertIsNotNone(result)
        self.assertEqual(result.mail, employee.mail)
        self.assertEqual(result.first_name, employee.first_name)
        self.assertEqual(result.role_name, "Developer")
        self.assertEqual(result.access_label, "Employee")
        self.assertEqual(result.access_level, 1)

    def test_login_returns_none_when_mail_is_unknown(self):
        service = LoginService(FakeEmployeeRepository({}))

        result = service.login("unknown@company.be", "hash")

        self.assertIsNone(result)

    def test_login_returns_none_when_password_is_wrong(self):
        employee = self.make_employee()
        service = LoginService(FakeEmployeeRepository({employee.mail: employee}))

        result = service.login("test@company.be", "wrong")

        self.assertIsNone(result)

    def test_login_returns_none_when_employee_is_deleted(self):
        employee = self.make_employee(is_deleted=True)
        service = LoginService(FakeEmployeeRepository({employee.mail: employee}))

        result = service.login("test@company.be", "hash")

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
