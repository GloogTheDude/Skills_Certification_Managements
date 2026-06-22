from db.repositories.diploma_repository import DiplomaRepository
from db.repositories.domaine_repository import DomaineRepository
from dto.diploma_dto import DiplomaCrudDTO
from models.diploma import Diploma


class DiplomaService:
    def __init__(
        self,
        diploma_repository: DiplomaRepository,
        domaine_repository: DomaineRepository | None = None,
    ):
        self.diploma_repository = diploma_repository
        self.domaine_repository = domaine_repository

    def get_all(self) -> list[Diploma]:
        return self.diploma_repository.get_all()

    def get_by_id(self, id_diploma: int) -> Diploma | None:
        return self.diploma_repository.get_by_id(id_diploma)

    def create(
        self,
        subject_diploma: str,
        level_diploma: str,
        id_domaine: int,
    ) -> Diploma | None:
        if self.domaine_repository is not None:
            domaine = self.domaine_repository.get_by_id(id_domaine)

            if domaine is None or domaine.is_deleted:
                return None

        diploma = Diploma()
        diploma.subject_diploma = subject_diploma
        diploma.level_diploma = level_diploma
        diploma.id_domaine = id_domaine
        diploma.is_deleted = False

        return self.diploma_repository.add(diploma)

    def update(
        self,
        id_diploma: int,
        subject_diploma: str,
        level_diploma: str,
        id_domaine: int,
    ) -> Diploma | None:
        diploma = self.diploma_repository.get_by_id(id_diploma)

        if diploma is None or diploma.is_deleted:
            return None

        if self.domaine_repository is not None:
            domaine = self.domaine_repository.get_by_id(id_domaine)

            if domaine is None or domaine.is_deleted:
                return None

        diploma.subject_diploma = subject_diploma
        diploma.level_diploma = level_diploma
        diploma.id_domaine = id_domaine

        return diploma

    def delete(self, id_diploma: int) -> bool:
        diploma = self.diploma_repository.get_by_id(id_diploma)

        if diploma is None or diploma.is_deleted:
            return False

        self.diploma_repository.soft_delete(diploma)
        return True
    
    def get_all_for_crud(self) -> list[DiplomaCrudDTO]:
        rows = self.diploma_repository.get_all_for_crud()

        return [
            DiplomaCrudDTO(
                id_diploma=id_diploma,
                subject_diploma=subject_diploma,
                level_diploma=level_diploma,
                id_domaine=id_domaine,
                domaine_name=domaine_name,
            )
            for id_diploma, subject_diploma, level_diploma, id_domaine, domaine_name in rows
        ]