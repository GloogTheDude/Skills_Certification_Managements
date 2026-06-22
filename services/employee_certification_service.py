
from datetime import date
from dateutil.relativedelta import relativedelta

from db.repositories.employee_certification_repository import EmployeeCertificationRepository
from models.certification import Certification
from models.employee_certification import EmployeeCertification

class EmployeeCertificationService():
    def __init__(self, employee_certification_repository: EmployeeCertificationRepository):
        self.employee_certification_repository = employee_certification_repository
    
    def add(self,id_employee:int, id_certification:int, start_:date, end_:date, organism:str, 
            validity_month:int, evaluation:str = None):
        employee_certification = EmployeeCertification()
        employee_certification.id_employee = id_employee
        employee_certification.id_certification = id_certification
        employee_certification.start_ = start_
        employee_certification.end_ = end_
        employee_certification.is_deleted = False
        employee_certification.organism = organism
        employee_certification.evaluation = evaluation
        if validity_month is None or end_ is None: 
            employee_certification.expiration =None
        else: 
            employee_certification.expiration = end_ + relativedelta(months=validity_month)
        
        self.employee_certification_repository.add(employee_certification)