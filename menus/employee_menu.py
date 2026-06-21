from dto.employee_skill_dto import EmployeeSkillDTO
from dto.employee_certification_dto import EmployeeCertificationDTO
from dto.skill_dto import SkillProfileDTO

class EmployeeMenu():
    def __init__(self):
        pass
    
    def main_menu(self):
        user_choice =-1
        while not(0<=user_choice<=4): 
            print("Here are your options:")
            print("1. See skills")
            print("2. See certifications")
            print("3. Request training")
            print("4. Follow up on your requests")
            print("0. Leave")
            user_choice = int(input("Your choice: "))
        return user_choice
    
    def display_skills(self,skills_employee: list[SkillProfileDTO]):
        print("===============YOUR SKILLS=================")
        print(f"{'Skill':<12}|{'Level':<7}|{'From':<18}|Domaine")
        for es in skills_employee:
            print(f"{es.skill_name:<12}|{es.displayed_level:<7}|{es.primary_source.source_type:<18}|{es.skill_domaine}")
        print("===========================================")
    
    
    def display_certification(self, certifications_employee:list[EmployeeCertificationDTO]):
        print("==========YOUR CERTIFICATIONS==============")
        print(f"{'certifications':<25}|{'peremption':<10}|{'skills'}")
        for ec in certifications_employee:
            print(
                f"{ec.certification_name:<25}|{ec.expiration_date}|"
                f"{', '.join(f'{s.skill_name}({s.level})' for s in ec.skills)}")
        print("===========================================")
