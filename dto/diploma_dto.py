from dataclasses import dataclass


@dataclass
class DiplomaCrudDTO:
    id_diploma: int
    subject_diploma: str | None
    level_diploma: str | None
    id_domaine: int | None
    domaine_name: str | None