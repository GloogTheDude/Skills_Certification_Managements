import unittest
from datetime import date

from dateutil.relativedelta import relativedelta
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

from core.constants import PARTICIPATIONSTATUS
from models import Base
from models.access_level import AccessLevel
from models.role import Role
from models.employee import Employee
from models.domaine import Domaine
from models.training_source import TrainingSource
from models.certification import Certification
from models.diploma import Diploma
from models.training import Training
from models.participation import Participation
from models.employee_certification import EmployeeCertification
from models.employee_diploma import EmployeeDiploma

from db.repositories.participation_repository import ParticipationRepository
from db.repositories.employee_certification_repository import EmployeeCertificationRepository
from db.repositories.employee_diploma_repository import EmployeeDiplomaRepository

from services.participation_service import ParticipationService
from services.employee_certification_service import EmployeeCertificationService
from services.employee_diploma_service import EmployeeDiplomaService


class ParticipationCompletionWorkflowTestCase(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine("sqlite+pysqlite:///:memory:", echo=False)

        @event.listens_for(self.engine, "connect")
        def enable_foreign_keys(dbapi_connection, connection_record):
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.close()

        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.seed()

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)
        self.engine.dispose()

    def seed(self):
        self.session.add_all([
            AccessLevel(id_access_level=1, label="Employee", level=1),
            Role(id_role=1, denomination_role="Developer", id_access_level=1, is_deleted=False),

            Domaine(id_domaine=1, nom_domaine="Backend", is_deleted=False),
            TrainingSource(id_source=1, name_source="Technifutur", is_deleted=False),

            Employee(
                id_employee=4,
                first_name="David",
                last_name="Henrichmann",
                hash_password="hash",
                mail="david@example.com",
                id_role=1,
                id_manager=None,
                is_deleted=False,
            ),

            Certification(
                id_certification=1,
                subject_certification="Python Professional",
                id_domaine=1,
                validity_month=36,
                is_deleted=False,
            ),

            Diploma(
                id_diploma=1,
                subject_diploma="Bachelier Informatique",
                level_diploma="Bachelor",
                id_domaine=1,
                is_deleted=False,
            ),

            Training(
                id_training=1,
                title="Python Certification Training",
                id_domaine=1,
                id_source=1,
                id_certification=1,
                id_diploma=None,
                start_=date(2026, 1, 8),
                end_=date(2026, 1, 19),
                cost_hour=85,
                duration_hours=70,
                is_deleted=False,
            ),

            Training(
                id_training=2,
                title="Diploma Bridge Training",
                id_domaine=1,
                id_source=1,
                id_certification=None,
                id_diploma=1,
                start_=date(2026, 2, 1),
                end_=date(2026, 2, 20),
                cost_hour=75,
                duration_hours=120,
                is_deleted=False,
            ),

            Training(
                id_training=3,
                title="Skills Only Training",
                id_domaine=1,
                id_source=1,
                id_certification=None,
                id_diploma=None,
                start_=date(2026, 3, 1),
                end_=date(2026, 3, 2),
                cost_hour=0,
                duration_hours=14,
                is_deleted=False,
            ),

            Participation(
                id_employee=4,
                id_training=1,
                status=PARTICIPATIONSTATUS.IN_PROGRESS.value,
                is_deleted=False,
            ),
            Participation(
                id_employee=4,
                id_training=2,
                status=PARTICIPATIONSTATUS.IN_PROGRESS.value,
                is_deleted=False,
            ),
            Participation(
                id_employee=4,
                id_training=3,
                status=PARTICIPATIONSTATUS.IN_PROGRESS.value,
                is_deleted=False,
            ),
        ])
        self.session.commit()

    def test_set_participation_to_completed_changes_status(self):
        repo = ParticipationRepository(self.session)
        service = ParticipationService(repo)

        service.set_participation_to_completed(4, 3)
        self.session.commit()

        participation = repo.get_by_ids(4, 3)
        self.assertEqual(participation.status, PARTICIPATIONSTATUS.COMPLETED.value)

    def test_certification_training_creates_employee_certification(self):
        training = self.session.get(Training, 1)
        certification = self.session.get(Certification, 1)

        cert_repo = EmployeeCertificationRepository(self.session)
        cert_service = EmployeeCertificationService(cert_repo)

        cert_service.add(
            id_employee=4,
            id_certification=certification.id_certification,
            start_=training.start_,
            end_=training.end_,
            organism=training.source.name_source,
            validity_month=certification.validity_month,
            evaluation="passed",
        )

        part_repo = ParticipationRepository(self.session)
        part_service = ParticipationService(part_repo)
        part_service.set_participation_to_completed(4, 1)

        self.session.commit()

        created = (
            self.session.query(EmployeeCertification)
            .filter_by(id_employee=4, id_certification=1)
            .one()
        )

        self.assertEqual(created.start_, date(2026, 1, 8))
        self.assertEqual(created.end_, date(2026, 1, 19))
        self.assertEqual(created.expiration, date(2026, 1, 19) + relativedelta(months=36))
        self.assertEqual(created.organism, "Technifutur")
        self.assertEqual(created.evaluation, "passed")
        self.assertFalse(created.is_deleted)

        participation = part_repo.get_by_ids(4, 1)
        self.assertEqual(participation.status, PARTICIPATIONSTATUS.COMPLETED.value)

    def test_diploma_training_creates_employee_diploma(self):
        training = self.session.get(Training, 2)

        diploma_repo = EmployeeDiplomaRepository(self.session)
        diploma_service = EmployeeDiplomaService(diploma_repo)

        diploma_service.add(
            employee_id=4,
            diploma_id=training.id_diploma,
            start_=training.start_,
            end_=training.end_,
            distinction="GREAT",
            school=training.source.name_source,
        )

        part_repo = ParticipationRepository(self.session)
        part_service = ParticipationService(part_repo)
        part_service.set_participation_to_completed(4, 2)

        self.session.commit()

        created = (
            self.session.query(EmployeeDiploma)
            .filter_by(id_employee=4, id_diploma=1)
            .one()
        )

        self.assertEqual(created.start_, date(2026, 2, 1))
        self.assertEqual(created.end_, date(2026, 2, 20))
        self.assertEqual(created.school, "Technifutur")
        self.assertEqual(created.distinction, "GREAT")
        self.assertFalse(created.is_deleted)

        participation = part_repo.get_by_ids(4, 2)
        self.assertEqual(participation.status, PARTICIPATIONSTATUS.COMPLETED.value)

    def test_get_details_by_status_does_not_return_cartesian_product(self):
        repo = ParticipationRepository(self.session)

        rows = repo.get_details_by_status(PARTICIPATIONSTATUS.IN_PROGRESS.value)

        self.assertEqual(len(rows), 3)

        for participation, employee, training in rows:
            self.assertEqual(participation.id_employee, employee.id_employee)
            self.assertEqual(participation.id_training, training.id_training)


if __name__ == "__main__":
    unittest.main()