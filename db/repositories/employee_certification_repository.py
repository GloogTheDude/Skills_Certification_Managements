from sqlalchemy import select, func, or_
from sqlalchemy.orm import Session

from models.certification import Certification
from models.employee import Employee
from models.employee_certification import EmployeeCertification
from datetime import date
from dateutil.relativedelta import relativedelta

class EmployeeCertificationRepository():
    def __init__(self, session:Session):
        self.session = session

    def add(self, employee_certification:EmployeeCertification):
        self.session.add(employee_certification)

    def get_close_to_expiration(self)->list[tuple[EmployeeCertification,Employee, Certification]]:
        today = date.today()
        limit_future = today + relativedelta(months=6)
        limit_past = today - relativedelta(months=3)

        stmt = (
            select(EmployeeCertification, Employee, Certification)
            .join(Employee, EmployeeCertification.id_employee == Employee.id_employee)
            .join(
                Certification,
                EmployeeCertification.id_certification == Certification.id_certification
            )
            .where(
                EmployeeCertification.expiration.is_not(None),

                # expire in the next 6 months or expired in the last 3 months
                EmployeeCertification.expiration >= limit_past,
                EmployeeCertification.expiration <= limit_future,

                EmployeeCertification.is_deleted.is_(False),
                Employee.is_deleted.is_(False),
                Certification.is_deleted.is_(False),
            )
        )
        return self.session.execute(stmt).all()