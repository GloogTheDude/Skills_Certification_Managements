from db.repositories.participation_repository import ParticipationRepository

class ServiceParticipation():
    
    def __init__(self, participation_repository:ParticipationRepository):
        self.participation_repository = participation_repository

    def complete_participation(self):
        pass
        