from sqlalchemy import select
from sqlalchemy.orm import Session

from models.certification_skill import CertificationSkill


class CertificationSkillRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_by_certification_id(
        self,
        id_certification: int,
    ) -> list[CertificationSkill]:
        stmt = select(CertificationSkill).where(
            CertificationSkill.id_certification == id_certification
        )
        return self.session.scalars(stmt).all()

    def add(self, certification_skill: CertificationSkill) -> CertificationSkill:
        self.session.add(certification_skill)
        return certification_skill