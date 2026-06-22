
from dto.participation_dto import ParticipationDTO

class ParticipationMenu():
    def __init__(self):
        pass
    
    @staticmethod
    def get_participation_dto(participation_dict: dict[int:ParticipationDTO]):
        user_choice=-1
        while not(0<=user_choice<=len(participation_dict)):
            for key, dto in participation_dict.items():
                print(f"{key}: {dto.employee_first_name} {dto.employee_last_name} - {dto.training_title} - {dto.training_end} - {dto.participation_status}")
            print("0: Leave")
            user_choice = int(input("your choice: "))  

        if user_choice == 0:
            return None
        else:
            return participation_dict[user_choice]


    @staticmethod
    def main_menu():
        user_choice = -1
        while not(0<=user_choice<=2):
            print("What do you want to do?")
            print("1. Complete participation" )
            print("2. Update training participation status")
            print("3. Create a participation to a training for an employee")
            print("0. Leave")
            user_choice = int(input("your choice: "))
        return user_choice
        