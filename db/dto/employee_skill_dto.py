from dataclasses import dataclass

@dataclass
class EmployeeSkillDTO:
    skill_name: str
    level: int