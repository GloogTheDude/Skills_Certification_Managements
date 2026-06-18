from dto.training_dto import TrainingSummaryDTO
from dto.training_request_dto import TrainingRequestDTO
from models.domaine import Domaine

class TrainingRequestMenu():

    def main_menu(self)->int:
        user_choice = -1
        while not(0<= user_choice<=3) :
            print("1. See all near formations")
            print("2. Request a place at an already planned formation")
            print("3. Request a personalised training")
            print("0. Back")
            user_choice = int(input("Your choice: "))
        print(f"will return {user_choice}")
        return user_choice

    def display_training(self, trainings:dict[TrainingSummaryDTO], filter:set[str]=None):
        for k,v in trainings.items():
            if not filter or len(filter)==0:
                print(f"{k} - {v.title} - {v.domaine_name} - {v.start_date} - {v.end_date}")
            else:
                if v.domaine_name in filter:
                    print(f"{k} - {v.title} - {v.domaine_name} - {v.start_date} - {v.end_date}")
    
    def add_filter_domaine_menu(self, 
                            domaines_set:set[str]=None)->str|None:
        user_input=-1
        domaine_list = sorted(list(domaines_set))
        while user_input not in range(len(domaine_list)+1): 
            for i in range(len(domaine_list)):
                print(f"{i+1}- {domaine_list[i]}")
            print("0 - go back")
            try:
                user_input = int(input("your choice: "))
            except ValueError:
                print("Invalid choice")
                continue

        if user_input == 0:
            return None
        return domaine_list[user_input-1]
    
    def remove_filter_domaine_menu(self,  
                            domaine_filter:set[str]=None):
        user_input = -1
        domaine_list = sorted(list(domaine_filter))
        while user_input not in range(len(domaine_list)+1): 
            for i in range(len(domaine_list)):
                print(f"{i+1}- {domaine_list[i]}")
            print("0 - go back")
            try:
                user_input = int(input("your choice: "))
            except ValueError:
                print("Invalid choice")
                continue

        if user_input == 0:
            return None
        return domaine_list[user_input-1]
        

    def see_all_formation(self, trainings:list[TrainingSummaryDTO], filter:set[str]=None):
        print('in see_all_formation_menu')
        user_choice=-1
        while not(0<= user_choice <=3) :
            print("into the while")
            print("===================TRAININGS===========================")
            self.display_training(trainings, filter)
            print("=======================================================")
            print("Do would you like to:")
            print("1. filter the trainings by domaine")
            print("2. request a place at one of those")
            print("3. request a personalised training")
            print("4. follow on your requests")
            print("0. go back")
            user_choice = int(input("your choice: "))
        return user_choice
        
    def request_place_to_planned_training(self, trainings:list[TrainingSummaryDTO], filter:set[str]=None):
        user_choice=-1
        print("menu : request_place_to_planned_training")
        while not(0<=user_choice <= len(trainings)+1) :
            print("===================TRAININGS===========================")
            self.display_training(trainings, filter)
            print("=======================================================")
            print("select one you want to attempt or press (0) to leave:")
            user_choice = int(input("your choice: "))
        
        if user_choice == 0:
            return None
        return user_choice-1
        
    def request_personalised_training(self):
        print("You are asking for a personalised request, please enter the kind of extra-training you wish to follow:")
        desc = input()
        return desc
    
    def filter_modifications_menu(self):
        user_input = -1
        while not (0<= user_input<=2):
            print("1 - add domaines to filter in")
            print("2 - remove domaines from filter")
            print("0 - go back")
            user_input = int(input("your choice: "))
        return user_input
    
    def display_employee_requests(self,employee_requests:list[TrainingRequestDTO]):
        user_input = -1
        while not(0 <= user_input <= len(employee_requests)+1):
            print("========================TRAINING REQUESTS================================")
            for i in range(len(employee_requests)):
                print(f"{i+1} - {employee_requests[i].training_title} - {employee_requests[i].status}")

            print("=========================================================================")
            print("Choose on to see details, (0) to leave")
            user_input = int(input("your choice: "))
        
        if user_input ==0:
            return
        return employee_requests[user_input-1]
    
    def display_employee_request_details(self,employe_request:TrainingRequestDTO):
        print("================================DETAILS===================================")
        print(f"TRAININGS: {employe_request.training_title} - {employe_request.domaine_name}")
        print(f"REQUESTED: {employe_request.requested_at}")
        print(f"STATUS: {employe_request.status}")
        print(f"YOUR ASK: {employe_request.request_desc}")
        print(f"RESPONSE: {employe_request.reason}")
        print("=========================================================================")

    def display_domaines_available(self, domaines_available:list[Domaine]):
        user_choice = -1
        while not(0<=user_choice<=len(domaines_available)+1):
            print("THE EXISTINGS DOMAINES:")
            for i in range(len(domaines_available)):
                print(f"{i+1}- {domaines_available[i].nom_domaine}")
            print("0 - Leave")
            user_choice = int(input("your choice: "))
        if user_choice == 0:
            return
        else:
            return domaines_available[i-1]
        
    def personalised_training_request_menu(self):
        request = input("Please ask us what you exeptect: ")
        return request