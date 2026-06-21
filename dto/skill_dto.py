from dataclasses import dataclass


@dataclass
class SkillProfileDTO:
    skill_id:int
    skill_name:str
    active_level:int|None
    historical_level:int|None
    source: list[dict[str:int]]
    status:str