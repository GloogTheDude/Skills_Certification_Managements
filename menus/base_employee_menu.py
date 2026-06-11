

class BaseEmployeeMenu():
    def __init__(self):
        pass
    def menu(self):
        user_choice =-1
        while not(0<=user_choice<=3): 
            print("Here are your options:")
            print("1. See skills")
            print("2. See certifications")
            print("3. Request training")
            print("0. Leave")
            user_choice = int(input("Your choice: "))
        return user_choice