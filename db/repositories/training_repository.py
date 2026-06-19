from sqlalchemy import select, func, or_
from sqlalchemy.orm import Session

from models.training import Training
from models.domaine import Domaine
from models.training_request import TrainingRequest
from models.training_skill import TrainingSkill
from models.skill import Skill

from datetime import date
from dto.training_skill_dto import TrainingSkillDTO


class TrainingRepository():
    def __init__(self, session: Session):
        self.session = session

    def get_future_trainings(self, id_employee: int):
        subquery = (
            select(TrainingRequest.id_training)
            .where(
                TrainingRequest.id_employee == id_employee,
                TrainingRequest.id_training.is_not(None),
            )
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
                Training.start_ > date.today(),
                Training.id_training.not_in(subquery),
                Training.is_deleted.is_(False),
                Domaine.is_deleted.is_(False),
            )
        )

        return self.session.execute(stmt).all()

    def get_by_id(self, id_training)->Training:
        return self.session.get(Training, id_training)
    
    def get_skills_by_id_training(self, id_training)->tuple[Training,TrainingSkill,Skill]:
        stmt = (
            select(Training,
                   TrainingSkill,
                   Skill)
                   .join(
                       TrainingSkill.id_training == Training.id_training,
                       Skill.id_skill == TrainingSkill.id_skill
                   )
                   .where(Training.id_training == id_training)
        )
        return self.session.execute(stmt).all()