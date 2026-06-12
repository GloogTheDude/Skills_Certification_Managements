from dto.employee_skill_dto import EmployeeSkillDTO

class EmployeeMenu():
    def __init__(self):
        pass
    
    def main_menu(self):
        user_choice =-1
        while not(0<=user_choice<=3): 
            print("Here are your options:")
            print("1. See skills")
            print("2. See certifications")
            print("3. Request training")
            print("0. Leave")
            user_choice = int(input("Your choice: "))
        return user_choice
    
    def display_skills(self,skills_employee: list[EmployeeSkillDTO]):
        print("===============YOUR SKILLS=================")
        print(f"{'Skill':<12} | {'Level':<7}")
        for es in skills_employee:
            print(f"{es.skill_name:<12} - {es.level:<7}")
        print("===========================================")
    
    def display_certification(self, certifications_employee:list(EmployeeCertificationDTO)):
        