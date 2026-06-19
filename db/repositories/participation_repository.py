from sqlalchemy import select, func
from sqlalchemy.orm import Session

from models.participation import Participation

class ParticipationRepository():
    def __init__(self, session:Session):
        self.session = session

    def add(self,participation:Participation):
        self.session.add(participation)