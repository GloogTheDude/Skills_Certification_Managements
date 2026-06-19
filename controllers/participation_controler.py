from core.database import SessionLocal
from db.repositories.participation_repository import ParticipationRepository 
from services.participation_service import ParticipationService

from dto.participation_dto import ParticipationDTO
from menus.participation_menu import ParticipationMenu as pm

class ParticipationController():
    def __init__(self):
        pass

    def complete_participation(self):
        #récupérer participation:
            #make menu to get participation
        #récupérer training
        #déterminer si training donne diplôme / certification
        #récupérer les skills directs du training
        #si diplôme : récupérer les skills du diplôme
        #si certification : récupérer les skills de la certification
        #fusionner les skills obtenus
        #créer EmployeeXDiploma ou EmployeeXCertification si pertinent
        #créer/mettre à jour les validations de skills
        #marquer la participation comme completed
        #commit
        pass

    def complete_participation(self):
        participations_completable={}
        with SessionLocal() as session:
            repo = ParticipationRepository(session)
            service = ParticipationService(repo)
            participations_completable = service.get_participations_completable()
        
        participation_selected:ParticipationDTO = pm.get_participation_dto(participations_completable)

    