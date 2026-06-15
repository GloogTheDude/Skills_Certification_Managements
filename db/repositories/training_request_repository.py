from sqlalchemy import select, func, or_, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models.training_request import TrainingRequest
from models.training import Training
from models.domaine import Domaine

class TrainingRequestRepository():
    def __init__(self, session: Session):
        self.session = session

    def add_request_preplanned_training(self,
                                        training_request: TrainingRequest):
        try:
            self.session.add(training_request)
            self.session.commit()

        except SQLAlchemyError:
            self.session.rollback()
            raise
    
    def get_employee_request(self, id_employee: int):
        stmt = (
            select(
                TrainingRequest,
                Training.title,
                Domaine.nom_domaine,
            )
            .outerjoin(TrainingRequest.training)
            .outerjoin(Training.domaine)
            .where(TrainingRequest.id_employee == id_employee)
        )
        return self.session.execute(stmt).all()

    def get_domaines_available(self):
        stmt = (
            select(
                Domaine
            )
            .where(
                Domaine.is_deleted.is_(False),
            )
        )
        return self.session.execute(stmt).all()

