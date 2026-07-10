from dataclasses import dataclass
from datetime import date


@dataclass
class SkillSourceDTO:
    source_type: str
    source_id: int
    level: int
    is_active: bool
    acquired_at: date | None = None
    expires_at: date | None = None


@dataclass
class SkillProfileDTO:
    skill_id: int
    skill_name: str
    skill_domaine:str
    displayed_level: int
    primary_source: SkillSourceDTO | None
    sources: list[SkillSourceDTO]

@dataclass
class SkillCrudDTO:
    id_skill: int
    name_skill: str
    domaine_name: str | None
