from sqlalchemy import select, func
from sqlalchemy.orm import Session

from models.employee import Employee
from models.role import Role


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
    
    def delete(self,employee:Employee)->None:
        self.session.delete(employee)
        self.session.commit()
    
    def get_by_role(self, role_name: str) -> list[Employee]:
        stmt = (
            select(Employee)
            .join(Role)
            .where(Role.denomination_role == role_name)
        )
        return self.session.scalars(stmt).all()
    
    def get_by_mail(self, mail:str)-> Employee|None:
        stmt=(
            select(Employee)
            .where(Employee.mail == mail)
        )
        return self.session.scalar(stmt)

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