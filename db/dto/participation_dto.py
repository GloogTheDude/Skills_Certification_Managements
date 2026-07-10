from dataclasses import dataclass
from datetime import date

@dataclass
class ParticipationDTO:
    employee_id : int
    employee_first_name: str
    employee_last_name:str
    
    training_id: int
    training_title: str
    training_start:date
    training_end:date

    training_type:str

    participation_status: str
