from sqlalchemy import select, func, or_
from sqlalchemy.orm import Session

from models.domaine import Domaine

class DomaineRepository():
    def __init__(self, session: Session):
        self.session = session

    def get_domaines(self):
        stmt = (
            select(
                Domaine
            )
            .where(
                Domaine.is_deleted.is_(False),
            )
        )
        return self.session.execute(stmt).all()
