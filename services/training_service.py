from db.repositories.training_repository import TrainingRepository
from models.training import Training
from dto.training_dto import TrainingSummaryDTO

class TrainingService():

    def __init__(self, training_repository:TrainingRepository):
        self.training_repository  = training_repository
    
    def fetch_available_training(self, employee_id:int):
        results = self.training_repository.get_future_trainings(employee_id)
        trainings:dict[int: TrainingSummaryDTO] = {}
        i=1
        print(f"****** {type(results)} - {results}********")
        for t,d in results:
            ts = TrainingSummaryDTO(
                    id_training=t.id_training,
                    title=t.title,
                    domaine_name= d,
                    start_date= t.start_,
                    end_date= t.end_
                )
            trainings[i]=ts
            i+=1
        return trainings

    def filter_dto_by_domaine_name(self,trainings_availables: dict[int, TrainingSummaryDTO]
                                   ,domaine_filter:set[str]):
        domaines = set()
        for k,v in trainings_availables.items():
            domaines.add(v.domaine_name)
        domaines.difference_update(domaine_filter)

        return domaines
    
    
            
