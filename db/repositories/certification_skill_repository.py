from sqlalchemy import select

from models.certification_skill import CertificationSkill


class CertificationSkillRepository:
    def __init__(self, session):
        self.session = session

    def add(self, certification_skill):
        self.session.add(certification_skill)

    def get_by_certification_id(self, id_certification):
        stmt = select(CertificationSkill).where(
            CertificationSkill.id_certification == id_certification,
            CertificationSkill.is_deleted.is_(False)
        )
        return self.session.scalars(stmt).all()

    def soft_delete_by_certification_id(self, id_certification):
        links = self.get_by_certification_id(id_certification)
        for link in links:
            link.is_deleted = True