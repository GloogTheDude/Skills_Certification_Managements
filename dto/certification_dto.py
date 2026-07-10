from dataclasses import dataclass


@dataclass
class CertificationCrudDTO:
    id_certification: int
    subject_certification: str | None
    validity_month: int | None
    id_domaine: int | None
    domaine_name: str | None