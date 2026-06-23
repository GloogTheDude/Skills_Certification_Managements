import unittest
from datetime import date
from decimal import Decimal

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

from models import Base
from models.access_level import AccessLevel
from models.role import Role
from models.employee import Employee
from models.domaine import Domaine
from models.training_source import TrainingSource
from models.skill import Skill
from models.diploma import Diploma
from models.certification import Certification
from models.diploma_skill import DiplomaSkill
from models.certification_skill import CertificationSkill
from models.training import Training
from models.training_skill import TrainingSkill

from db.repositories.employee_repository import EmployeeRepository
from db.repositories.role_repository import RoleRepository
from db.repositories.domaine_repository import DomaineRepository
from db.repositories.training_source_repository import TrainingSourceRepository
from db.repositories.diploma_repository import DiplomaRepository
from db.repositories.certification_repository import CertificationRepository
from db.repositories.diploma_skill_repository import DiplomaSkillRepository
from db.repositories.certification_skill_repository import CertificationSkillRepository
from db.repositories.training_repository import TrainingRepository
from db.repositories.training_skill_repository import TrainingSkillRepository

from services.employee_service import EmployeeService
from services.diploma_service import DiplomaService
from services.certification_service import CertificationService
from services.training_service import TrainingService


class CrudWorkflowTestCase(unittest.TestCase):
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
        self.session.add_all(
            [
                AccessLevel(id_access_level=1, label="Employee", level=1),
                AccessLevel(id_access_level=2, label="Manager", level=2),
                AccessLevel(id_access_level=3, label="HR", level=3),

                Role(
                    id_role=1,
                    denomination_role="Developer",
                    id_access_level=1,
                    is_deleted=False,
                ),
                Role(
                    id_role=2,
                    denomination_role="Manager",
                    id_access_level=2,
                    is_deleted=False,
                ),
                Role(
                    id_role=3,
                    denomination_role="Deleted Role",
                    id_access_level=1,
                    is_deleted=True,
                ),

                Domaine(id_domaine=1, nom_domaine="Backend", is_deleted=False),
                Domaine(id_domaine=2, nom_domaine="Deleted Domain", is_deleted=True),

                TrainingSource(
                    id_source=1,
                    name_source="Technifutur",
                    is_deleted=False,
                ),
                TrainingSource(
                    id_source=2,
                    name_source="Deleted Source",
                    is_deleted=True,
                ),

                Skill(id_skill=1, name_skill="Python", id_domaine=1, is_deleted=False),
                Skill(id_skill=2, name_skill="SQL", id_domaine=1, is_deleted=False),
                Skill(id_skill=3, name_skill="Git", id_domaine=1, is_deleted=False),

                Employee(
                    id_employee=1,
                    first_name="Alice",
                    last_name="Manager",
                    hash_password="hash_alice",
                    mail="alice@example.com",
                    id_role=2,
                    id_manager=None,
                    is_deleted=False,
                ),
                Employee(
                    id_employee=2,
                    first_name="David",
                    last_name="Henrichmann",
                    hash_password="hash_david",
                    mail="david@example.com",
                    id_role=1,
                    id_manager=1,
                    is_deleted=False,
                ),

                Diploma(
                    id_diploma=1,
                    subject_diploma="Bachelor IT",
                    level_diploma="Bachelor",
                    id_domaine=1,
                    is_deleted=False,
                ),

                Certification(
                    id_certification=1,
                    subject_certification="Python Professional",
                    validity_month=36,
                    id_domaine=1,
                    is_deleted=False,
                ),
            ]
        )
        self.session.commit()

    def test_employee_create_valid(self):
        service = EmployeeService(
            EmployeeRepository(self.session),
            RoleRepository(self.session),
        )

        created = service.create(
            first_name="Nora",
            last_name="Dev",
            mail="nora@example.com",
            hash_password="hash_nora",
            id_role=1,
            id_manager=1,
        )

        self.session.commit()

        self.assertIsNotNone(created)
        self.assertEqual(created.mail, "nora@example.com")
        self.assertFalse(created.is_deleted)

    def test_employee_create_rejects_duplicate_mail(self):
        service = EmployeeService(
            EmployeeRepository(self.session),
            RoleRepository(self.session),
        )

        created = service.create(
            first_name="Duplicate",
            last_name="User",
            mail="david@example.com",
            hash_password="hash",
            id_role=1,
            id_manager=1,
        )

        self.assertIsNone(created)

    def test_employee_create_rejects_deleted_role(self):
        service = EmployeeService(
            EmployeeRepository(self.session),
            RoleRepository(self.session),
        )

        created = service.create(
            first_name="Bad",
            last_name="Role",
            mail="bad.role@example.com",
            hash_password="hash",
            id_role=3,
            id_manager=None,
        )

        self.assertIsNone(created)

    def test_employee_update_rejects_self_manager(self):
        service = EmployeeService(
            EmployeeRepository(self.session),
            RoleRepository(self.session),
        )

        updated = service.update(
            id_employee=2,
            first_name="David",
            last_name="Henrichmann",
            mail="david@example.com",
            hash_password=None,
            id_role=1,
            id_manager=2,
        )

        self.assertIsNone(updated)

    def test_employee_soft_delete(self):
        service = EmployeeService(EmployeeRepository(self.session))

        deleted = service.delete(2)
        self.session.commit()

        employee = self.session.get(Employee, 2)

        self.assertTrue(deleted)
        self.assertTrue(employee.is_deleted)

    def test_diploma_replace_skills_creates_links(self):
        service = DiplomaService(
            DiplomaRepository(self.session),
            DomaineRepository(self.session),
            DiplomaSkillRepository(self.session),
        )

        result = service.replace_skills(
            id_diploma=1,
            skill_levels=[(1, 3), (2, 2)],
        )

        self.session.commit()

        links = (
            self.session.query(DiplomaSkill)
            .filter_by(id_diploma=1, is_deleted=False)
            .all()
        )

        self.assertTrue(result)
        self.assertEqual(len(links), 2)
        self.assertEqual(
            {link.id_skill: link.min_level for link in links},
            {1: 3, 2: 2},
        )

    def test_diploma_replace_skills_soft_deletes_removed_links(self):
        service = DiplomaService(
            DiplomaRepository(self.session),
            DomaineRepository(self.session),
            DiplomaSkillRepository(self.session),
        )

        service.replace_skills(1, [(1, 3), (2, 2)])
        self.session.flush()

        service.replace_skills(1, [(1, 4)])
        self.session.commit()

        active_links = (
            self.session.query(DiplomaSkill)
            .filter_by(id_diploma=1, is_deleted=False)
            .all()
        )
        deleted_link = (
            self.session.query(DiplomaSkill)
            .filter_by(id_diploma=1, id_skill=2)
            .one()
        )

        self.assertEqual(len(active_links), 1)
        self.assertEqual(active_links[0].id_skill, 1)
        self.assertEqual(active_links[0].min_level, 4)
        self.assertTrue(deleted_link.is_deleted)

    def test_certification_replace_skills_creates_links(self):
        service = CertificationService(
            CertificationRepository(self.session),
            DomaineRepository(self.session),
            CertificationSkillRepository(self.session),
        )

        result = service.replace_skills(
            id_certification=1,
            skill_levels=[(1, 4), (3, 2)],
        )

        self.session.commit()

        links = (
            self.session.query(CertificationSkill)
            .filter_by(id_certification=1, is_deleted=False)
            .all()
        )

        self.assertTrue(result)
        self.assertEqual(len(links), 2)
        self.assertEqual(
            {link.id_skill: link.granted_level for link in links},
            {1: 4, 3: 2},
        )

    def test_training_create_rejects_no_target_and_no_skills(self):
        service = TrainingService(
            TrainingRepository(self.session),
            DomaineRepository(self.session),
            TrainingSourceRepository(self.session),
            DiplomaRepository(self.session),
            CertificationRepository(self.session),
            TrainingSkillRepository(self.session),
        )

        created = service.create(
            title="Invalid Training",
            id_domaine=1,
            id_source=1,
            start_=date(2026, 1, 1),
            end_=date(2026, 1, 2),
            cost_hour=Decimal("100.00"),
            duration_hours=Decimal("8.00"),
            id_diploma=None,
            id_certification=None,
            skill_levels=[],
        )

        self.assertIsNone(created)

    def test_training_create_rejects_diploma_and_certification_together(self):
        service = TrainingService(
            TrainingRepository(self.session),
            DomaineRepository(self.session),
            TrainingSourceRepository(self.session),
            DiplomaRepository(self.session),
            CertificationRepository(self.session),
            TrainingSkillRepository(self.session),
        )

        created = service.create(
            title="Invalid XOR Training",
            id_domaine=1,
            id_source=1,
            start_=date(2026, 1, 1),
            end_=date(2026, 1, 2),
            cost_hour=Decimal("100.00"),
            duration_hours=Decimal("8.00"),
            id_diploma=1,
            id_certification=1,
            skill_levels=[],
        )

        self.assertIsNone(created)

    def test_training_create_skills_only_then_replace_skills(self):
        service = TrainingService(
            TrainingRepository(self.session),
            DomaineRepository(self.session),
            TrainingSourceRepository(self.session),
            DiplomaRepository(self.session),
            CertificationRepository(self.session),
            TrainingSkillRepository(self.session),
        )

        created = service.create(
            title="Python Basics",
            id_domaine=1,
            id_source=1,
            start_=date(2026, 1, 1),
            end_=date(2026, 1, 2),
            cost_hour=Decimal("100.00"),
            duration_hours=Decimal("8.00"),
            id_diploma=None,
            id_certification=None,
            skill_levels=[(1, 2), (2, 1)],
        )

        self.assertIsNotNone(created)

        self.session.flush()

        service.replace_skills(
            created.id_training,
            [(1, 2), (2, 1)],
        )

        self.session.commit()

        links = (
            self.session.query(TrainingSkill)
            .filter_by(id_training=created.id_training, is_deleted=False)
            .all()
        )

        self.assertEqual(len(links), 2)
        self.assertEqual(
            {link.id_skill: link.granted_level for link in links},
            {1: 2, 2: 1},
        )

    def test_training_create_with_diploma_without_skills_is_valid(self):
        service = TrainingService(
            TrainingRepository(self.session),
            DomaineRepository(self.session),
            TrainingSourceRepository(self.session),
            DiplomaRepository(self.session),
            CertificationRepository(self.session),
            TrainingSkillRepository(self.session),
        )

        created = service.create(
            title="Bachelor Bridge",
            id_domaine=1,
            id_source=1,
            start_=date(2026, 2, 1),
            end_=date(2026, 2, 20),
            cost_hour=Decimal("75.00"),
            duration_hours=Decimal("120.00"),
            id_diploma=1,
            id_certification=None,
            skill_levels=[],
        )

        self.session.commit()

        self.assertIsNotNone(created)
        self.assertEqual(created.id_diploma, 1)
        self.assertIsNone(created.id_certification)

    def test_training_create_rejects_deleted_domain(self):
        service = TrainingService(
            TrainingRepository(self.session),
            DomaineRepository(self.session),
            TrainingSourceRepository(self.session),
            DiplomaRepository(self.session),
            CertificationRepository(self.session),
            TrainingSkillRepository(self.session),
        )

        created = service.create(
            title="Deleted Domain Training",
            id_domaine=2,
            id_source=1,
            start_=date(2026, 1, 1),
            end_=date(2026, 1, 2),
            cost_hour=Decimal("100.00"),
            duration_hours=Decimal("8.00"),
            id_diploma=None,
            id_certification=None,
            skill_levels=[(1, 2)],
        )

        self.assertIsNone(created)

    def test_training_create_rejects_deleted_source(self):
        service = TrainingService(
            TrainingRepository(self.session),
            DomaineRepository(self.session),
            TrainingSourceRepository(self.session),
            DiplomaRepository(self.session),
            CertificationRepository(self.session),
            TrainingSkillRepository(self.session),
        )

        created = service.create(
            title="Deleted Source Training",
            id_domaine=1,
            id_source=2,
            start_=date(2026, 1, 1),
            end_=date(2026, 1, 2),
            cost_hour=Decimal("100.00"),
            duration_hours=Decimal("8.00"),
            id_diploma=None,
            id_certification=None,
            skill_levels=[(1, 2)],
        )

        self.assertIsNone(created)


if __name__ == "__main__":
    unittest.main()