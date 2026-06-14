from services.training_service import TrainingService
from models.employee import Employee
from menus.training_request_menu import TrainingRequestMenu
from services.training_request_service import TrainingRequestService

class TrainingRequestController():
    
    def __init__(self, training_service:TrainingService, training_request_service: TrainingRequestService,employee: Employee):
        self.training_service = training_service
        self.employee = employee
        self.training_request_service = training_request_service
        self.training_request_menu = TrainingRequestMenu()

    def get_training_request_menu(self):
        
        domaine_filter = set()
        user_choice = -1
        while user_choice !=0:
            trainings_availables = self.training_service.fetch_available_training(self.employee.id_employee)
            user_choice = self.training_request_menu.main_menu()
            print(f"in controler user_choice = {user_choice}")
            match user_choice:
                case 0:
                    return
                case 1:
                    print("case 1")
                    self.see_all_info(self.training_request_menu,trainings_availables,domaine_filter)
                case 2:
                    self.select_preplaned_training(self.training_request_menu,
                                                   trainings_availables,
                                                   domaine_filter)
                case 3:
                    self.make_personalised_request()
                case 4:
                    self.follow_up_request()

    def see_all_info(self, 
                    trainings_availables:dict, 
                    domaine_filter:set):
        user_choice = -1
        while not (0<=user_choice<=3):
            user_choice = self.training_request_menu.see_all_formation(trainings=trainings_availables,
                                                                  filter= domaine_filter)
            match user_choice:
                case 0:
                    return
                case 1:
                    self.handle_filter_modification(trainings_availables, 
                                                    domaine_filter)
                case 2:
                    self.select_preplaned_training(trainings_availables,
                                                   domaine_filter)
                case 3:
                    self.make_personalised_request()
    
    def add_domaine_to_filter(self, trainings_availables:dict,domaine_filter:set):
        domaines:set = self.training_service.filter_dto_by_domaine_name(trainings_availables,domaine_filter)
        while domaines:
            domaine = self.training_request_menu.add_filter_domaine_menu(domaines)
            if domaine is None:
                return
            domaine_filter.add(domaine)
            domaines.remove(domaine)
        print("No more domaines to filter")
        return
    
    def remove_domaine_from_filter(self,domaine_filter: set[str],):
        if not domaine_filter:
            print("No active domaine filter")
            return
        while domaine_filter:
            domaine = self.training_request_menu.remove_filter_domaine_menu(domaine_filter
            )
            if domaine is None:
                return
            domaine_filter.remove(domaine)

    def handle_filter_modification(self,trainings_availables:dict,domaine_filter:set):
        while True:
            user_input = self.training_request_menu.filter_modifications_menu()
            match user_input:
                case 0:
                    return
                case 1: self.add_domaine_to_filter(self.training_request_menu, 
                                                trainings_availables,
                                                domaine_filter)
                case 2: self.remove_domaine_from_filter(self.training_request_menu,
                                                domaine_filter)



    def select_preplaned_training(self,trainings_availables:dict,domaine_filter:set):
        user_choice = -1
        while not (0<=user_choice<=len(trainings_availables)+1):
            user_choice = self.training_request_menu.request_place_to_planned_training(
                                                                trainings=trainings_availables,
                                                                filter= domaine_filter)
        if user_choice == 0:
            return None
        
        print(f"You asked to follow :{trainings_availables[user_choice].title}")
        self.training_request_service.call_add_request_preplanned_training(self.employee,trainings_availables[user_choice])
    

    
    def make_personalised_request(self):
        request_desc = self.training_request_menu.personalised_training_request_menu()
        self.training_request_service.call_add_request_personalised_training(self.employee,request_desc)

    def follow_up_request(self):
        print("FOLLOW UP")
        employee_requests=self.training_request_service.get_employee_request(self.employee)
        while True:
            print("WHILE")
            user_choice = self.training_request_menu.display_employee_requests(employee_requests)
            if user_choice is None:
                return
            self.training_request_menu.display_employee_request_details(user_choice)

