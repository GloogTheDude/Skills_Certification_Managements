from sqlalchemy import select, func, or_
from sqlalchemy.orm import Session

from models.training import Training
from models.domaine import Domaine
from models.training_request import TrainingRequest

class TrainingRepository():
    def __init__(self, session: Session):
        self.session = session

    def get_future_trainings(self, id_employee: int):
        subquery = (
            select(TrainingRequest.id_training)
            .where(TrainingRequest.id_employee == id_employee)
        )

        stmt = (
            select(
                Training,
                Domaine.nom_domaine,
            )
            .join(
                Domaine,
                Training.id_domaine == Domaine.id_domaine,
            )
            .where(
                Training.start_ > func.current_date(),
                Training.id_training.not_in(subquery),
                Training.is_deleted.is_(False),
                Domaine.is_deleted.is_(False),
            )
        )

        return self.session.execute(stmt).all()