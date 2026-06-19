from sqlalchemy import select, func,and_
from sqlalchemy.orm import Session

from models.participation import Participation
from models.employee import Employee
from models.training import Training

from datetime import date

class ParticipationRepository():
    def __init__(self, session:Session):
        self.session = session

    def add(self,participation:Participation):
        self.session.add(participation)
    
    def get_by_ids(self, id_employee,id_training):
        return self.session.get(Participation, (id_employee,id_training))
    
    def get_by_status(self, status):
        stmt = (
            select(Participation)
            .where(
                Participation.status == status,
                Participation.is_deleted.is_(False)
            )
        )
        return self.session.scalars(stmt).all()
    
    def get_details_by_status(self, status, max_end_date:date|None = None):
        conditions = [
            Participation.status == status,
            Participation.is_deleted.is_(False),
            Employee.is_deleted.is_(False),
            Training.is_deleted.is_(False)
        ]
        if max_end_date is not None:
            conditions.append(Training.end_ <= max_end_date)
        stmt = (
            select(...)
            .where(*conditions)
        )
        return self.session.execute(stmt).all()
    
