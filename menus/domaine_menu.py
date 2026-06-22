from models.domaine import Domaine


class DomaineMenu:
    @staticmethod
    def main_menu() -> int:
        user_choice = -1

        while not (0 <= user_choice <= 4):
            print("===== DOMAINE CRUD =====")
            print("1. List domaines")
            print("2. Create domaine")
            print("3. Update domaine")
            print("4. Delete domaine")
            print("0. Leave")

            user_choice = int(input("Your choice: "))

        return user_choice

    @staticmethod
    def display_domaines(domaines: list[Domaine]) -> None:
        print("===== DOMAINES =====")

        if not domaines:
            print("No domaine found.")
            return

        for domaine in domaines:
            print(f"{domaine.id_domaine}: {domaine.nom_domaine}")

    @staticmethod
    def ask_id_domaine() -> int:
        return int(input("Domaine id: "))

    @staticmethod
    def ask_nom_domaine() -> str:
        return input("Domaine name: ").strip()

    @staticmethod
    def display_success(message: str) -> None:
        print(message)

    @staticmethod
    def display_error(message: str) -> None:
        print(message)