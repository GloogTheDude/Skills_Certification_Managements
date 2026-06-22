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


@dataclass
class EmployeeCrudDTO:
    id_employee: int
    first_name: str | None
    last_name: str | None
    mail: str | None
    id_role: int | None
    role_name: str | None
    id_manager: int | None
    manager_name: str | None