from sqlalchemy import select
from sqlalchemy.orm import Session

from models.training_source import TrainingSource


class TrainingSourceRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[TrainingSource]:
        stmt = (
            select(TrainingSource)
            .where(TrainingSource.is_deleted.is_(False))
            .order_by(TrainingSource.id_source)
        )
        return self.session.scalars(stmt).all()

    def get_by_id(self, id_training_source: int) -> TrainingSource | None:
        return self.session.get(TrainingSource, id_training_source)

    def add(self, training_source: TrainingSource) -> TrainingSource:
        self.session.add(training_source)
        return training_source

    def soft_delete(self, training_source: TrainingSource) -> None:
        training_source.is_deleted = True