from models.training_source import TrainingSource


class TrainingSourceMenu:
    @staticmethod
    def main_menu() -> int:
        user_choice = -1

        while not (0 <= user_choice <= 4):
            print("===== TRAINING SOURCE CRUD =====")
            print("1. List training sources")
            print("2. Create training source")
            print("3. Update training source")
            print("4. Delete training source")
            print("0. Leave")

            user_choice = int(input("Your choice: "))

        return user_choice

    @staticmethod
    def display_training_sources(training_sources: list[TrainingSource]) -> None:
        print("===== TRAINING SOURCES =====")

        if not training_sources:
            print("No training source found.")
            return

        for source in training_sources:
            print(f"{source.id_source}: {source.name_source}")

    @staticmethod
    def ask_name_source() -> str:
        return input("Training source name: ").strip()

    @staticmethod
    def ask_id_source() -> int:
        return int(input("Training source id: "))

    @staticmethod
    def display_success(message: str) -> None:
        print(message)

    @staticmethod
    def display_error(message: str) -> None:
        print(message)