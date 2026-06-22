from sqlalchemy import select
from sqlalchemy.orm import Session

from models.domaine import Domaine
from models.skill import Skill


class SkillRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[Skill]:
        stmt = (
            select(Skill)
            .where(Skill.is_deleted.is_(False))
            .order_by(Skill.id_skill)
        )
        return self.session.scalars(stmt).all()

    def get_by_id(self, id_skill: int) -> Skill | None:
        return self.session.get(Skill, id_skill)

    def add(self, skill: Skill) -> Skill:
        self.session.add(skill)
        return skill

    def soft_delete(self, skill: Skill) -> None:
        skill.is_deleted = True

    def get_all_for_crud(self):
        stmt = (
            select(Skill.id_skill, Skill.name_skill, Domaine.nom_domaine)
            .outerjoin(Domaine, Domaine.id_domaine == Skill.id_domaine)
            .where(Skill.is_deleted.is_(False))
            .order_by(Skill.id_skill)
        )
        return self.session.execute(stmt).all()