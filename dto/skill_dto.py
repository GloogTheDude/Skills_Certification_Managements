from dataclasses import dataclass


@dataclass
class SkillProfileDTO:
    skill_name:str
    active_level:int
    historical_level:int
    sources:int
    status:int