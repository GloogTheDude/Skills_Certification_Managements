from core.database import SessionLocal
from db.repositories.diploma_repository import DiplomaRepository
from db.repositories.employee_certification_repository import EmployeeCertificationRepository
from db.repositories.employee_diploma_repository import EmployeeDiplomaRepository
from db.repositories.employee_repository import EmployeeRepository
from db.repositories.participation_repository import ParticipationRepository 
from db.repositories.training_repository import TrainingRepository
from db.repositories.training_source_repository import TrainingSourceRepository
from models.certification import Certification
from models.employee import Employee
from models.training_source import TrainingSource
from services.diploma_service import DiplomaService
from services.employee_certification_service import EmployeeCertificationService
from services.employee_diploma_service import EmployeeDiplomaService
from services.employee_service import EmployeeService
from services.participation_service import ParticipationService

from core.constants import TYPEPARTICIPATIONDTO
from dto.participation_dto import ParticipationDTO
from menus.participation_menu import ParticipationMenu as pm
from services.training_service import TrainingService
from services.training_source_service import TrainingSourceService

class ParticipationController():
    def __init__(self):
        pass

    def complete_participation(self):
        participations_completable={}
        with SessionLocal() as session:
            repo_participation = ParticipationRepository(session)
            service = ParticipationService(repo_participation)
            participations_completable = service.get_participations_completable()
        
        participation_selected:ParticipationDTO = pm.get_participation_dto(participations_completable)

        if participation_selected.training_type == TYPEPARTICIPATIONDTO.DIPLOMA.value:
            self.complete_participation_diploma_training(participation_selected)
        elif participation_selected.training_type == TYPEPARTICIPATIONDTO.CERTIFICATION.value:
            self.complete_participation_certification_training(participation_selected) 
        
        with SessionLocal() as session:
            repo_participation = ParticipationRepository(session)
            service = ParticipationService(repo_participation)
            service.set_participation_to_completed(participation_selected.employee_id, participation_selected.training_id)


    def complete_participation_diploma_training(self, participation_selected:ParticipationDTO):
        with SessionLocal() as session:
            repo_training = TrainingRepository(session)
            repo_employee = EmployeeRepository(session)
            training_service= TrainingService(repo_training)
            employee_service = EmployeeService(repo_employee)
            training = training_service.get_by_id(participation_selected.training_id)
            employee = employee_service.get_by_id(participation_selected.employee_id)
            diploma_id = training.id_diploma
            training_source:TrainingSource = training.source

            distinction = "GREAT" #need a menu to get the distinction
            
            repo_employee_diploma = EmployeeDiplomaRepository(session)
            employee_diploma_service = EmployeeDiplomaService(repo_employee_diploma)
            employee_diploma_service.add(employee.id_employee, diploma_id, training.start_, training.end_, distinction, training_source.name_source)

    def complete_participation_certification_training(self, participation_selected:ParticipationDTO):
        with SessionLocal() as session:
            repo_training = TrainingRepository(session)
            repo_employee = EmployeeRepository(session)
            training_service= TrainingService(repo_training)
            employee_service = EmployeeService(repo_employee)
            training = training_service.get_by_id(participation_selected.training_id)
            employee:Employee = employee_service.get_by_id(participation_selected.employee_id)
            certification:Certification= training.certification
            training_source:TrainingSource = training.source
            
            repo_employee_certification = EmployeeCertificationRepository(session)
            employee_certification_service = EmployeeCertificationService(repo_employee_certification)
            employee_certification_service.add(employee.id_employee, certification.id_certification, training.start_, training.end, training_source.name_source, certification.validity_month)
    


