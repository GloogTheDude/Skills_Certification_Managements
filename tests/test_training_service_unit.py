import unittest
from datetime import date

from dto.training_dto import TrainingSummaryDTO
from models.training import Training
from services.training_service import TrainingService


class FakeTrainingRepository:
    def __init__(self, rows):
        self.rows = rows
        self.called_with_employee_id = None

    def get_future_trainings(self, employee_id: int):
        self.called_with_employee_id = employee_id
        return self.rows


class TestTrainingService(unittest.TestCase):
    def make_training(self):
        training = Training()
        training.id_training = 10
        training.title = "SQLAlchemy"
        training.start_ = date(2099, 1, 10)
        training.end_ = date(2099, 1, 12)
        return training

    def test_fetch_available_training_maps_repository_rows_to_indexed_dtos(self):
        training = self.make_training()
        repo = FakeTrainingRepository([(training, "Backend")])
        service = TrainingService(repo)

        result = service.fetch_available_training(employee_id=4)

        self.assertEqual(repo.called_with_employee_id, 4)
        self.assertEqual(list(result.keys()), [1])
        self.assertIsInstance(result[1], TrainingSummaryDTO)
        self.assertEqual(result[1].id_training, 10)
        self.assertEqual(result[1].title, "SQLAlchemy")
        self.assertEqual(result[1].domaine_name, "Backend")
        self.assertEqual(result[1].start_date, date(2099, 1, 10))
        self.assertEqual(result[1].end_date, date(2099, 1, 12))

    def test_filter_dto_by_domaine_name_returns_domaines_not_already_filtered(self):
        service = TrainingService(FakeTrainingRepository([]))
        trainings = {
            1: TrainingSummaryDTO(1, "Python", "Backend", None, None),
            2: TrainingSummaryDTO(2, "SQL", "Database", None, None),
            3: TrainingSummaryDTO(3, "Docker", "DevOps", None, None),
        }

        result = service.filter_dto_by_domaine_name(trainings, {"Backend"})

        self.assertEqual(result, {"Database", "DevOps"})


if __name__ == "__main__":
    unittest.main()
