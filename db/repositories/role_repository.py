from sqlalchemy import select
from sqlalchemy.orm import Session

from models.role import Role


class RoleRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[Role]:
        stmt = (
            select(Role)
            .where(Role.is_deleted.is_(False))
            .order_by(Role.id_role)
        )
        return self.session.scalars(stmt).all()

    def get_by_id(self, id_role: int) -> Role | None:
        return self.session.get(Role, id_role)