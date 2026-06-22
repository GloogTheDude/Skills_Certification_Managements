from sqlalchemy import select, func, or_
from sqlalchemy.orm import Session

from models.diploma import Diploma
from models.training import Training

class DiplomaRepository():
    def __init__(self,session:Session):
        self.session = session

    def get_by_id(self, id_diploma:int)->Diploma:
        return self.session.get(Diploma,id_diploma) 
    
    def get_by_training_id(self, id_training:int)->Diploma:
        training:Training = self.session(Training, id_training)
        return self.session.get(Diploma, training.id_diploma)