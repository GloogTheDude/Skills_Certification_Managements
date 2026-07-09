
from db.repositories.search_employee_skills_repository import SearchEmployeeSkillRepository
from dto.search_employee_dto import SearchEmployeeDTO


class SearchEmployeeSkillsService:
    def __init__(self, repo_employee_skill:SearchEmployeeSkillRepository):
        self.repo_employee_skill = repo_employee_skill 
    
    def fetch_employee_skills(self)->dict[int:SearchEmployeeDTO]:
        dict_dto = {}
        result = self.repo_employee_skill.fetch_skills_employee()
        #print(f"result = {result}")
        #struc result: id_employee, first_name, last_name, id_skill, name_skill, level
        for r in result:
            if r[0] in dict_dto.keys():
                if r[3] not in dict_dto[r[0]].skills:
                    dict_dto[r[0]].skills[r[3]] = [r[4],r[5]]
                    continue

            dto = SearchEmployeeDTO(
                id_employee= r[0],
                first_name= r[1],
                last_name=r[2],
                skills = {r[3]:[r[4],r[5]]} 
            )
            dict_dto[r[0]]=dto

        return dict_dto
    
