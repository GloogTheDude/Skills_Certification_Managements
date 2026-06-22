from datetime import date

from sqlalchemy import select
from sqlalchemy.orm import Session

from dto.training_skill_dto import TrainingSkillDTO
from models.certification import Certification
from models.diploma import Diploma
from models.domaine import Domaine
from models.skill import Skill
from models.training import Training
from models.training_request import TrainingRequest
from models.training_skill import TrainingSkill
from models.training_source import TrainingSource


class TrainingRepository:
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

    def get_all(self) -> list[Training]:
        stmt = (
            select(Training)
            .where(Training.is_deleted.is_(False))
            .order_by(Training.id_training)
        )
        return self.session.scalars(stmt).all()

    def get_all_for_crud(self):
        stmt = (
            select(
                Training.id_training,
                Training.title,
                Domaine.nom_domaine,
                TrainingSource.name_source,
                Certification.subject_certification,
                Diploma.subject_diploma,
                Training.start_,
                Training.end_,
                Training.cost_hour,
                Training.duration_hours,
            )
            .outerjoin(Domaine, Domaine.id_domaine == Training.id_domaine)
            .outerjoin(TrainingSource, TrainingSource.id_source == Training.id_source)
            .outerjoin(
                Certification,
                Certification.id_certification == Training.id_certification,
            )
            .outerjoin(Diploma, Diploma.id_diploma == Training.id_diploma)
            .where(Training.is_deleted.is_(False))
            .order_by(Training.id_training)
        )
        return self.session.execute(stmt).all()

    def get_by_id(self, id_training: int) -> Training | None:
        return self.session.get(Training, id_training)

    def add(self, training: Training) -> Training:
        self.session.add(training)
        return training

    def soft_delete(self, training: Training) -> None:
        training.is_deleted = True

    def get_skills_by_id_training(
        self,
        id_training: int,
    ) -> list[tuple[Training, TrainingSkill, Skill]]:
        stmt = (
            select(Training, TrainingSkill, Skill)
            .join(TrainingSkill, TrainingSkill.id_training == Training.id_training)
            .join(Skill, Skill.id_skill == TrainingSkill.id_skill)
            .where(Training.id_training == id_training)
        )
        return self.session.execute(stmt).all()

    def fetch_source(self, id_training: int) -> TrainingSource | None:
        training = self.get_by_id(id_training)

        if training is None:
            return None

        return training.source