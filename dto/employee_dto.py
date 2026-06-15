from dataclasses import dataclass

@dataclass
class EmployeeDTO:
    id_employee: int
    first_name: str
    last_name: str
    mail: str

    id_role: int
    role_name: str

    access_label: str
    access_level: int