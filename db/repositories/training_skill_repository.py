from sqlalchemy import select
from sqlalchemy.orm import Session

from models.training_skill import TrainingSkill


class TrainingSkillRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_by_training_id(self, id_training: int) -> list[TrainingSkill]:
        stmt = select(TrainingSkill).where(
            TrainingSkill.id_training == id_training
        )
        return self.session.scalars(stmt).all()

    def add(self, training_skill: TrainingSkill) -> TrainingSkill:
        self.session.add(training_skill)
        return training_skill