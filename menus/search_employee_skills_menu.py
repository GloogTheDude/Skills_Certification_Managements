
import operator

from dto.search_employee_dto import SearchEmployeeDTO
from dto.skill_dto import SkillCrudDTO
from menus.skill_menu import SkillMenu as sm


class SearchEmployeeSkillsMenu():
    def __init__(self):
        pass
    
    @staticmethod
    def main_menu(employees:dict[int: SearchEmployeeDTO], requisite:dict, skills:list[SkillCrudDTO]):
        SearchEmployeeSkillsMenu.display_list(employees)
        user_choice = -1
        while not(0<=user_choice<=2):
            print("1. add to filter")
            print("2. remove from filter")
            print("0. leave")
            user_choice = int(input("your choice: "))
        if user_choice ==0:
            return
        match user_choice:
            case 1:
                result = SearchEmployeeSkillsMenu.add_skill_to_filter(requisite, skills)
                requisite[result[0]]["condition"] = result[1]
                requisite[result[0]]["level"] = result[2]
            case 2:
                pass
            case _:
                print("you shouldn't be there")
                                
    @staticmethod
    def display_list(employees:dict[int: SearchEmployeeDTO]):
        #print(employees)
        for e in employees.values():
            printable = (f"{e.id_employee} - {e.first_name} {e.last_name}")
            skills = ""
            for s in e.skills.values():
                skills +=(f"[{s[0]}:{s[1]}]")
            print(f"{printable} - {skills}")
    
    @staticmethod 
    def display_filtered_list(employees:dict[int: SearchEmployeeDTO], requisite:list[dict]):
        print("==================FILTERED=================")
        for e in employees.values():
            is_printable =  True
            for r in requisite:
                if r["id"] not in e.skills:
                    is_printable = False
                    break
                if not (r["op"](e.skills[r["id"]][1],r["lvl"])): #this will blow up in my face
                    is_printable = False                        #r["op"] contain a function corresponding to an equivalance (<,<=,==,>= or >)
                    continue
            if is_printable:
                printable = (f"{e.id_employee} - {e.first_name} {e.last_name}")
                skills = ""
                for s in e.skills.values():
                    skills +=(f"[{s[0]}:{s[1]}]")
                print(f"{printable} - {skills}")

    @staticmethod
    def add_skill_to_filter(requisite:dict, skills:list[SkillCrudDTO]):
        skill_choice=-1
        while skill_choice not in requisite or skill_choice!=0:
            SearchEmployeeSkillsMenu.display_skills(skills, requisite)
            print("0.leave")
            skill_choice = int(input("your choice"))
        if skill_choice ==0:
            return 
        
        condition_choice=-1
        while not(0<=condition_choice <=5):
            print("1. >")
            print("2. >=")
            print("3. =")
            print("4. <=")
            print("5. <")
            print("0. leave")
            condition_choice = int(input("your choice"))
        
        if condition_choice ==0:
            return
        op = None 
        match condition_choice:
            case 1:
                op = operator.gt   # >
            case 2 :
                op = operator.ge   # >=
            case 3:
                op = operator.eq   # ==
            case 4:
                op = operator.le   # <=
            case 5:
                op = operator.lt   # <

        level = -1
        while not(0<=level<=5):
            print("level requiered(between 1 and 5 - 0 to cancel):")
            level = int(input("your choice"))
        
        if level ==0:
            return
        return{"id":skill_choice,"op":op, "lvl":level}


    def display_skills(skills: list[SkillCrudDTO], filter:dict) -> None:
        print("===== SKILLS =====")
        if not skills:
            print("No skill found.")
            return
        for skill in skills:
            if skill.id_skill in filter: 
                domaine_name = skill.domaine_name or "No domain"
                print(f"{skill.id_skill}: {skill.name_skill} - {domaine_name}")

