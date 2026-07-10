from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class TrainingSummaryDTO:
    id_training: int
    title: str
    domaine_name: str
    start_date: date
    end_date: date


@dataclass
class TrainingCrudDTO:
    id_training: int
    title: str | None
    domaine_name: str | None
    source_name: str | None
    certification_name: str | None
    diploma_name: str | None
    start_: date | None
    end_: date | None
    cost_hour: Decimal | None
    duration_hours: Decimal | None