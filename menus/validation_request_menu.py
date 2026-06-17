from dto.training_request_dto import PendingTrainingRequestForManagerDTO

class ValidationRequestMenu():

    def select_pending_request_to_update(self, pending_requests:list[PendingTrainingRequestForManagerDTO]):
        user_choice = -1
        while not(0<=user_choice<= len(pending_requests)):  
            print("================================PENDING REQUESTS==================================")
            if len(pending_requests)>0:
                for i in range(len(pending_requests)):
                    print(f"{i+1} - {pending_requests[i].first_name_employee} {pending_requests[i].last_name_employee} - {pending_requests[i].training_title} - {pending_requests[i].domaine_name}")
                print("0 - leave")
                user_choice = int(input("Your choice: "))
            else:
                print("No more Pending requests")
                return
        if user_choice == 0:
            return None
        return pending_requests[user_choice-1]
    
    def select_new_request_status(self):
        user_choice= -1
        while not(0<= user_choice <=2):
            print("Do you wish to: ")
            print("1. validate request")
            print("2. refuse request, we'll need a reason for that")
            print("0. cancel")
            user_choice = int(input("Your choice: "))
        return user_choice
    
    def get_reason(self):
        reason = ""
        while not reason.strip():
            reason = input("Please enter the reasoning: ") 
        return reason