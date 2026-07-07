class CrudMenu():
    @staticmethod
    def main_menu():
        print("int the  main_menu CRUD")
        user_choice = -1
        while not(0<=user_choice <=7):
            print("Choose what you want to CRUD:")
            print("1. CRUD Training source")
            print("2. CRUD Skill")
            print("3. CRUD Domaine")
            print("4. CRUD Diploma")
            print("5. CRUD Certification")
            print("6. CRUD Training")
            print("7. CRUD Employee")
            print("0. Leave")
            user_choice = int(input("Your choice: "))
        return user_choice