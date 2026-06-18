from sqlalchemy import select, func, or_, insert
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models.training_request import TrainingRequest
from models.training import Training
from models.domaine import Domaine
from models.employee import Employee

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
    
    def get_pending_request_for_manager(self, id_manager: int):
        stmt = (
            select(
                TrainingRequest,
                Employee,
                Training,
                Domaine.nom_domaine,
            )
            .join(TrainingRequest.employee)
            .outerjoin(TrainingRequest.training)
            .outerjoin(Training.domaine)
            .where(
                TrainingRequest.status == "pending",
                TrainingRequest.is_deleted.is_(False),
                Employee.id_manager == id_manager,
            )
        )

        return self.session.execute(stmt).all()
    
    def get_pending_request_for_hr(self):
        stmt = (
            select(
                TrainingRequest,
                Employee,
                Training,
                Domaine.nom_domaine,
            )
            .join(TrainingRequest.employee)
            .outerjoin(TrainingRequest.training)
            .outerjoin(Training.domaine)
            .where(
                TrainingRequest.status == "pending",
                TrainingRequest.is_deleted.is_(False),
            )
        )

        return self.session.execute(stmt).all()

    def update_request_status(self, id_request: int,
                                status: str,
                                reason: str | None = None,
                                id_validator: int | None = None) -> TrainingRequest | None:
        
        request = self.session.get(TrainingRequest, id_request)

        if request is None:
            return None

        if request.is_deleted:
            return None

        if id_validator is None:
            return None
        
        request.status = status
        request.reason = reason

        if id_validator is not None:
            request.id_validator = id_validator

        self.session.commit()
        self.session.refresh(request)

        return request