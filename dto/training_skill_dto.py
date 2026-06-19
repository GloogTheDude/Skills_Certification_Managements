from dataclasses import dataclass
 

@dataclass
class TrainingSkillDTO:
    training_id:int
    training_title:str
    skill_id:int
    skill_name:str
    granted_level:int