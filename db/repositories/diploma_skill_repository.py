from sqlalchemy import select

from models.diploma_skill import DiplomaSkill


class DiplomaSkillRepository:
    def __init__(self, session):
        self.session = session

    def add(self, diploma_skill):
        self.session.add(diploma_skill)

    def get_by_diploma_id(self, id_diploma):
        stmt = select(DiplomaSkill).where(
            DiplomaSkill.id_diploma == id_diploma,
            DiplomaSkill.is_deleted.is_(False)
        )
        return self.session.scalars(stmt).all()

    def soft_delete_by_diploma_id(self, id_diploma):
        links = self.get_by_diploma_id(id_diploma)
        for link in links:
            link.is_deleted = True