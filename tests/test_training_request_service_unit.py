import unittest
from datetime import date

from core.constants import TRAININGREQUESTSTATUS
from dto.training_dto import TrainingSummaryDTO
from dto.training_request_dto import TrainingRequestDTO
from models.employee import Employee
from models.training_request import TrainingRequest
from services.training_request_service import TrainingRequestService


class FakeTrainingRequestRepository:
    def __init__(self, rows=None):
        self.rows = rows or []
        self.added_requests = []
        self.called_with_employee_id = None

    def add_request_preplanned_training(self, training_request: TrainingRequest):
        self.added_requests.append(training_request)

    def get_employee_request(self, id_employee: int):
        self.called_with_employee_id = id_employee
        return self.rows

    def get_domaines_available(self):
        return []


class TestTrainingRequestService(unittest.TestCase):
    def make_employee(self):
        employee = Employee()
        employee.id_employee = 4
        return employee

    def test_call_add_request_preplanned_training_builds_pending_request(self):
        repo = FakeTrainingRequestRepository()
        service = TrainingRequestService(repo)
        employee = self.make_employee()
        training = TrainingSummaryDTO(
            id_training=9,
            title="REST API Design",
            domaine_name="Backend",
            start_date=None,
            end_date=None,
        )

        service.call_add_request_preplanned_training(employee, training)

        self.assertEqual(len(repo.added_requests), 1)
        created = repo.added_requests[0]
        self.assertEqual(created.id_employee, 4)
        self.assertEqual(created.id_training, 9)
        self.assertEqual(created.status, TRAININGREQUESTSTATUS.PENDING.value)
        self.assertEqual(created.requested_at, date.today())
        self.assertIsNone(created.reason)
        self.assertIsNone(created.request_desc)
        self.assertIsNone(created.id_validator)

    def test_call_add_request_personalised_training_builds_pending_request_without_training_id(self):
        repo = FakeTrainingRequestRepository()
        service = TrainingRequestService(repo)
        employee = self.make_employee()

        service.call_add_request_personalised_training(employee, "Formation Kubernetes")

        self.assertEqual(len(repo.added_requests), 1)
        created = repo.added_requests[0]
        self.assertEqual(created.id_employee, 4)
        self.assertIsNone(created.id_training)
        self.assertEqual(created.request_desc, "Formation Kubernetes")
        self.assertEqual(created.status, TRAININGREQUESTSTATUS.PENDING.value)

    def test_get_employee_request_maps_rows_to_complete_dtos(self):
        tr = TrainingRequest()
        tr.id_training_request = 42
        tr.request_desc = None
        tr.status = "PENDING"
        tr.reason = "Useful for project"
        tr.requested_at = date(2026, 6, 1)
        tr.is_deleted = False
        tr.id_employee = 4
        tr.id_training = 9
        tr.id_validator = 2

        repo = FakeTrainingRequestRepository(rows=[(tr, "REST API Design", "Backend")])
        service = TrainingRequestService(repo)
        employee = self.make_employee()

        result = service.get_employee_request(employee)

        self.assertEqual(repo.called_with_employee_id, 4)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], TrainingRequestDTO)
        self.assertEqual(result[0].id_training_request, 42)
        self.assertEqual(result[0].request_desc, None)
        self.assertEqual(result[0].status, "PENDING")
        self.assertEqual(result[0].reason, "Useful for project")
        self.assertEqual(result[0].requested_at, date(2026, 6, 1))
        self.assertFalse(result[0].is_deleted)
        self.assertEqual(result[0].id_employee, 4)
        self.assertEqual(result[0].id_training, 9)
        self.assertEqual(result[0].id_validator, 2)
        self.assertEqual(result[0].training_title, "REST API Design")
        self.assertEqual(result[0].domaine_name, "Backend")


if __name__ == "__main__":
    unittest.main()
