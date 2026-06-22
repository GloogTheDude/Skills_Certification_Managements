from db.repositories.diploma_repository import DiplomaRepository
from db.repositories.employee_diploma_repository import EmployeeDiplomaRepository
from models.diploma import Diploma
from models.employee_diploma import EmployeeDiploma
from datetime import date

class DiplomaService():
    def __init__(self, diploma_repository:DiplomaRepository):
        self.diploma_repository = diploma_repository
    
    def get_by_id(self, id_diploma)->Diploma:
        return self.diploma_repository.get_by_id(id_diploma)