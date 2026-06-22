from db.repositories.employee_repository import EmployeeRepository
from models.employee import Employee
from dto.employee_dto import EmployeeDTO

class EmployeeService():
    def __init__(self, employee_repository:EmployeeRepository):
        self.employee_repository =  employee_repository

    def get_by_id(self, id_employee):
        return self.employee_repository.get_by_id(id_employee)