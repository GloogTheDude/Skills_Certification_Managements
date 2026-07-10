from dataclasses import dataclass
from datetime import date

@dataclass
class SearchEmployeeDTO():
    id_employee: int
    first_name: str
    last_name: str
    skills: dict
