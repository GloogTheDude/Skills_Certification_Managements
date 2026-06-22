from sqlalchemy import select, func
from sqlalchemy.orm import Session

from models.employee_diploma import EmployeeDiploma

class EmployeeDiplomaRepository():
    def __init__(self, session:Session):
        self.session = session

    def add(self, employee_diploma: EmployeeDiploma):
        self.session.add(employee_diploma)