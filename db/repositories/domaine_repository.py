from sqlalchemy import select
from sqlalchemy.orm import Session

from models.domaine import Domaine


class DomaineRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[Domaine]:
        stmt = (
            select(Domaine)
            .where(Domaine.is_deleted.is_(False))
            .order_by(Domaine.id_domaine)
        )
        return self.session.scalars(stmt).all()

    def get_by_id(self, id_domaine: int) -> Domaine | None:
        return self.session.get(Domaine, id_domaine)

    def add(self, domaine: Domaine) -> Domaine:
        self.session.add(domaine)
        return domaine

    def soft_delete(self, domaine: Domaine) -> None:
        domaine.is_deleted = True