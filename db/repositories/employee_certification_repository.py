from sqlalchemy import select, func, or_
from sqlalchemy.orm import Session

from models.employee_certification import EmployeeCertification

class EmployeeCertificationRepository():
    def __init__(self, session:Session):
        self.session = session

    def add(self, employee_certification:EmployeeCertification):
        self.session.add(employee_certification)