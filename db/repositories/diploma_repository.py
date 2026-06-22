from sqlalchemy import select
from sqlalchemy.orm import Session

from models.diploma import Diploma
from models.training import Training
from models.domaine import Domaine


class DiplomaRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[Diploma]:
        stmt = (
            select(Diploma)
            .where(Diploma.is_deleted.is_(False))
            .order_by(Diploma.id_diploma)
        )
        return self.session.scalars(stmt).all()

    def get_by_id(self, id_diploma: int) -> Diploma | None:
        return self.session.get(Diploma, id_diploma)

    def get_by_training_id(self, id_training: int) -> Diploma | None:
        training: Training | None = self.session.get(Training, id_training)

        if training is None or training.id_diploma is None:
            return None

        return self.session.get(Diploma, training.id_diploma)

    def add(self, diploma: Diploma) -> Diploma:
        self.session.add(diploma)
        return diploma

    def soft_delete(self, diploma: Diploma) -> None:
        diploma.is_deleted = True

    def get_all_for_crud(self):
        stmt = (
            select(
                Diploma.id_diploma,
                Diploma.subject_diploma,
                Diploma.level_diploma,
                Diploma.id_domaine,
                Domaine.nom_domaine,
            )
            .outerjoin(Domaine, Domaine.id_domaine == Diploma.id_domaine)
            .where(Diploma.is_deleted.is_(False))
            .order_by(Diploma.id_diploma)
        )

        return self.session.execute(stmt).all()