import unittest

from core.database import SessionLocal
from models.employee import Employee
from db.repositories.employee_repository import EmployeeRepository


class TestEmployeeRepository(unittest.TestCase):

    def setUp(self):
        self.session = SessionLocal()
        self.repo = EmployeeRepository(self.session)

    def tearDown(self):
        self.session.close()

    def test_get_by_id_existing_employee(self):
        employee = self.repo.get_by_id(4)

        self.assertIsNotNone(employee)
        self.assertIsInstance(employee, Employee)
        self.assertEqual(employee.first_name, "David")

    def test_get_by_id_unknown_employee_returns_none(self):
        employee = self.repo.get_by_id(999999)

        self.assertIsNone(employee)

    def test_get_all_returns_employees(self):
        employees = self.repo.get_all()

        self.assertIsInstance(employees, list)
        self.assertGreaterEqual(len(employees), 1)
        self.assertIsInstance(employees[0], Employee)

    def test_get_by_mail_existing_employee(self):
        employee = self.repo.get_by_mail("david.henrichmann@example.com")

        self.assertIsNotNone(employee)
        self.assertEqual(employee.first_name, "David")

    def test_get_by_mail_unknown_returns_none(self):
        employee = self.repo.get_by_mail("unknown@company.be")

        self.assertIsNone(employee)

    def test_get_by_role_returns_employee_list(self):
        employees = self.repo.get_by_role("Developer")

        self.assertIsInstance(employees, list)
        self.assertGreaterEqual(len(employees), 5)

        mails = [employee.mail for employee in employees]
        self.assertIn("david.henrichmann@example.com", mails)

    def test_get_subordinates_returns_employee_list(self):
        employees = self.repo.get_subordinates(1)

        self.assertIsInstance(employees, list)

        mails = [employee.mail for employee in employees]
        self.assertIn("marc.dubois@example.com", mails)

    def test_count_all(self):
        count = self.repo.count_all()

        self.assertIsInstance(count, int)
        self.assertGreaterEqual(count, 15)
    def test_save_and_delete_employee(self):
        employee = Employee(
            first_name="Test",
            last_name="User",
            hash_password="hash",
            mail="test.user@company.be",
            id_role=1,
            id_manager=2,
        )

        self.repo.save(employee)

        self.assertIsNotNone(employee.id_employee)

        saved_employee = self.repo.get_by_mail("test.user@company.be")
        self.assertIsNotNone(saved_employee)
        self.assertEqual(saved_employee.first_name, "Test")

        self.repo.delete(saved_employee)

        deleted_employee = self.repo.get_by_mail("test.user@company.be")
        self.assertIsNone(deleted_employee)


if __name__ == "__main__":
    unittest.main()