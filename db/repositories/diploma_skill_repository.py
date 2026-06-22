from sqlalchemy import select
from sqlalchemy.orm import Session

from models.diploma_skill import DiplomaSkill


class DiplomaSkillRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_by_diploma_id(self, id_diploma: int) -> list[DiplomaSkill]:
        stmt = select(DiplomaSkill).where(DiplomaSkill.id_diploma == id_diploma)
        return self.session.scalars(stmt).all()

    def add(self, diploma_skill: DiplomaSkill) -> DiplomaSkill:
        self.session.add(diploma_skill)
        return diploma_skill