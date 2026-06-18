from db.repositories.training_request_repository import TrainingRequestRepository
from dto.training_dto import TrainingSummaryDTO
from models.training_request import TrainingRequest
from models.employee import Employee
from models.training import Training
from core.constants import TRAININGREQUESTSTATUS
from datetime import datetime, date
from dto.training_request_dto import TrainingRequestDTO, PendingTrainingRequestForManagerDTO
from dto.employee_dto import EmployeeDTO

class TrainingRequestService():

    def __init__(self, training_request_repository:TrainingRequestRepository):
        self.training_request_repository= training_request_repository
    
    from datetime import date

    def call_add_request_preplanned_training(self,
                        employee: EmployeeDTO,
                        preplanned_training: TrainingSummaryDTO,):
        tr = TrainingRequest()

        tr.id_employee = employee.id_employee
        tr.id_training = preplanned_training.id_training
        tr.requested_at = date.today()
        tr.status = TRAININGREQUESTSTATUS.PENDING.value

        tr.reason = None
        tr.request_desc = None
        tr.id_validator = None

        try:
            self.training_request_repository.add_request_preplanned_training(tr)
            print("Request created")

        except Exception as e:
            print(f"Error: {e}")


    def call_add_request_personalised_training(self, employee:EmployeeDTO,request_desc:str):
        print("call_add_request_personalised_training")
        tr = TrainingRequest()

        tr.id_employee = employee.id_employee
        tr.id_training = None
        tr.requested_at = date.today()
        tr.status = TRAININGREQUESTSTATUS.PENDING.value

        tr.reason = None
        tr.request_desc = request_desc
        tr.id_validator = None
        try:
            self.training_request_repository.add_request_preplanned_training(tr)
            print("Request created")

        except Exception as e:
            print(f"Error: {e}")

    
    def get_employee_request(self, employee: EmployeeDTO) -> list[TrainingRequestDTO]:
        requests = self.training_request_repository.get_employee_request(
            employee.id_employee
        )
        result = []
        for tr, title, domaine_name in requests:
            dto = TrainingRequestDTO(
                id_training_request=tr.id_training_request,
                request_desc=tr.request_desc,

                status=tr.status,
                reason=tr.reason,
                requested_at=tr.requested_at,

                is_deleted=tr.is_deleted,

                id_employee=tr.id_employee,
                id_training=tr.id_training,
                id_validator=tr.id_validator,

                training_title=title,
                domaine_name=domaine_name,
            )
            result.append(dto)
        return result

    def get_available_domaines(self):
        return self.training_request_repository.get_domaines_available()
    
    def get_pending_request_for_manager(self, id_manager:int)->list[PendingTrainingRequestForManagerDTO]:
        rows = self.training_request_repository.get_pending_request_for_manager(id_manager)
        result =[]
        for tr, employee, training, domaine_name in rows:
            dto = PendingTrainingRequestForManagerDTO(
                id_training_request=tr.id_training_request,
                request_desc=tr.request_desc,

                status=tr.status,
                reason=tr.reason,
                requested_at=tr.requested_at,

                id_employee=tr.id_employee,
                first_name_employee = employee.first_name,
                last_name_employee= employee.last_name,
                id_training=tr.id_training,
                #id_validator=tr.id_validator,

                training_title= training.title if isinstance(training, Training) else None,
                domaine_name=domaine_name,
            )
            result.append(dto)
        return result

    def update_request_status(self, id_request, status, reason, id_validator ):
        self.training_request_repository.update_request_status(id_request, status, reason, id_validator )
