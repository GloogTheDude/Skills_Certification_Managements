from db.repositories.employee_repository import EmployeeRepository
from models.employee import Employee

class LoginService():
    
    def __init__(self, employee_repo:EmployeeRepository):
        self.employee_repo = employee_repo
    
    def login(self, mail:str, password:str):
        employee = self.employee_repo.get_by_mail(mail)
        if employee is None:
            return None
        
        # MVP temporaire : comparaison directe.
        # Plus tard : hash sécurisé.
        if employee.hash_password != password:
            return None
        
        if employee.is_deleted == True:
            return None
        
        return employee


