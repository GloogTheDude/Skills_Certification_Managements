from sqlalchemy import select, func
from sqlalchemy.orm import Session

from models.employee import Employee
from models.role import Role
from models.access_level import AccessLevel


class EmployeeRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, employee_id: int) -> Employee | None:
        #only because search via PK
        return self.session.get(
            Employee,
            employee_id
        )
    
    def get_all(self)->list[Employee]:
        stmt = select(Employee)
        return self.session.scalars(stmt).all()
    
    def save(self, employee:Employee)->None:
        self.session.add(employee)
        self.session.commit()
    
    def delete(self, employee: Employee) -> None:
        db_employee = self.session.get(Employee, employee.id_employee)
        if db_employee is not None:
            db_employee.is_deleted = True
            self.session.commit()
    
    def get_by_role(self, role_name: str) -> list[Employee]:
        stmt = (
            select(Employee)
            .join(Role)
            .where(Role.denomination_role == role_name)
        )
        return self.session.scalars(stmt).all()
    
    def get_by_mail_with_access(self, mail: str):
        stmt = (
            select(
                Employee,
                Role.denomination_role,
                AccessLevel.label,
                AccessLevel.level,
            )
            .join(Role, Employee.id_role == Role.id_role)
            .join(AccessLevel, Role.id_access_level == AccessLevel.id_access_level)
            .where(Employee.mail == mail)
        )

        return self.session.execute(stmt).first()

    def get_subordinates(self, id_manager:int)->list[Employee]:
        stmt=(
            select(Employee)
            .where(Employee.id_manager == id_manager)
        )
        return self.session.scalars(stmt).all()

    def count_all(self) -> int:
        stmt = select(
            func.count(Employee.id_employee)
        )

        return self.session.scalar(stmt)