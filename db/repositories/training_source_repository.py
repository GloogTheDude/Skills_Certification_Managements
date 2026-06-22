from sqlalchemy import select, func, or_
from sqlalchemy.orm import Session

from models.training_source import TrainingSource


class TrainingSourceRepository():
    def __init__(self, session:Session):
        self.session = session

    def get_by_id(self, id_training_source:int)->TrainingSource:
        return self.session.get(TrainingSource, id_training_source)
    