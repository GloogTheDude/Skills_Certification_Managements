

from db.repositories.training_source_repository import TrainingSourceRepository
from models.training_source import TrainingSource


class TrainingSourceService():
    def __init__(self, training_source_repository:TrainingSourceRepository):
        self.training_source_repository = training_source_repository
    
    def get_by_id(self, id_training_source)->TrainingSource:
        return self.training_source_repository(id_training_source)