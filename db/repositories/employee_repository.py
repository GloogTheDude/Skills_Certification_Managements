from sqlalchemy import select, func
from sqlalchemy.orm import Session, aliased

from models.employee import Employee
from models.role import Role
from models.access_level import AccessLevel


class EmployeeRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, employee_id: int) -> Employee | None:
        return self.session.get(Employee, employee_id)

    def get_all(self) -> list[Employee]:
        stmt = (
            select(Employee)
            .where(Employee.is_deleted.is_(False))
            .order_by(Employee.id_employee)
        )
        return self.session.scalars(stmt).all()

    def get_all_for_crud(self):
        Manager = aliased(Employee)

        stmt = (
            select(
                Employee.id_employee,
                Employee.first_name,
                Employee.last_name,
                Employee.mail,
                Employee.id_role,
                Role.denomination_role,
                Employee.id_manager,
                Manager.first_name,
                Manager.last_name,
            )
            .join(Role, Role.id_role == Employee.id_role)
            .outerjoin(Manager, Manager.id_employee == Employee.id_manager)
            .where(
                Employee.is_deleted.is_(False),
                Role.is_deleted.is_(False),
            )
            .order_by(Employee.id_employee)
        )

        return self.session.execute(stmt).all()

    def add(self, employee: Employee) -> Employee:
        self.session.add(employee)
        return employee

    def soft_delete(self, employee: Employee) -> None:
        employee.is_deleted = True

    def get_by_role(self, role_name: str) -> list[Employee]:
        stmt = (
            select(Employee)
            .join(Role)
            .where(
                Role.denomination_role == role_name,
                Employee.is_deleted.is_(False),
                Role.is_deleted.is_(False),
            )
        )
        return self.session.scalars(stmt).all()

    def get_by_mail(self, mail: str) -> Employee | None:
        stmt = (
            select(Employee)
            .where(
                Employee.mail == mail,
                Employee.is_deleted.is_(False),
            )
        )
        return self.session.scalar(stmt)

    def get_by_mail_with_access(self, mail: str):
        stmt = (
            select(
                Employee,
                Role.denomination_role,
                AccessLevel.label,
                AccessLevel.level,
            )
            .join(Employee.role)
            .join(Role.access_level)
            .where(
                Employee.mail == mail,
                Employee.is_deleted.is_(False),
                Role.is_deleted.is_(False),
                AccessLevel.id_access_level.is_not(None),
            )
        )

        return self.session.execute(stmt).first()

    def get_subordinates(self, id_manager: int) -> list[Employee]:
        stmt = (
            select(Employee)
            .where(
                Employee.id_manager == id_manager,
                Employee.is_deleted.is_(False),
            )
        )
        return self.session.scalars(stmt).all()

    def count_all(self) -> int:
        stmt = select(func.count(Employee.id_employee)).where(
            Employee.is_deleted.is_(False)
        )
        return self.session.scalar(stmt)