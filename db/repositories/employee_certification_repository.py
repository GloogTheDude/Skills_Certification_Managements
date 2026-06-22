from sqlalchemy import select, func, or_
from sqlalchemy.orm import Session

from models.employee_certification import EmployeeCertification

class EmployeeCertificationRepository():
    def __init__(self, session:Session):
        self.session = Session

    def add(self, employee_certification:EmployeeCertification):
        self.session.add(EmployeeCertification,employee_certification)