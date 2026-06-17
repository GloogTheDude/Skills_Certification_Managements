from dataclasses import dataclass
from datetime import date

@dataclass
class TrainingRequestDTO:
    id_training_request: int
    request_desc: str | None

    status: str
    reason: str | None
    requested_at: date

    is_deleted: bool

    id_employee: int
    id_training: int | None
    id_validator: int | None

    training_title: str | None
    domaine_name: str | None

@dataclass
class PendingTrainingRequestForManagerDTO():
    id_training_request: int
    request_desc: str | None

    status: str
    reason: str | None
    requested_at: date

    id_employee: int
    first_name_employee:str
    last_name_employee:str
    id_training: int | None

    training_title: str | None
    domaine_name: str | None
