from dataclasses import dataclass
from datetime import date

@dataclass
class TrainingSummaryDTO:
    id_training: int
    title: str
    domaine_name: str
    start_date: date | None
    end_date: date | None