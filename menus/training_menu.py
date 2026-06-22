from datetime import date
from decimal import Decimal

from dto.training_dto import TrainingCrudDTO


class TrainingMenu:
    @staticmethod
    def main_menu() -> int:
        user_choice = -1

        while not (0 <= user_choice <= 4):
            print("===== TRAINING CRUD =====")
            print("1. List trainings")
            print("2. Create training")
            print("3. Update training")
            print("4. Delete training")
            print("0. Leave")

            user_choice = int(input("Your choice: "))

        return user_choice

    @staticmethod
    def display_trainings(trainings: list[TrainingCrudDTO]) -> None:
        print("===== TRAININGS =====")

        if not trainings:
            print("No training found.")
            return

        for training in trainings:
            target = "Skills only"

            if training.certification_name:
                target = f"Certification: {training.certification_name}"
            elif training.diploma_name:
                target = f"Diploma: {training.diploma_name}"

            print(
                f"{training.id_training}: "
                f"{training.title} | "
                f"{training.domaine_name or 'No domain'} | "
                f"{training.source_name or 'No source'} | "
                f"{training.start_} -> {training.end_} | "
                f"{target} | "
                f"{training.cost_hour} €/h | "
                f"{training.duration_hours} h"
            )

    @staticmethod
    def ask_id_training() -> int:
        return int(input("Training id: "))

    @staticmethod
    def ask_title() -> str:
        return input("Training title: ").strip()

    @staticmethod
    def ask_id_domaine() -> int:
        return int(input("Domaine id: "))

    @staticmethod
    def ask_id_source() -> int:
        return int(input("Training source id: "))

    @staticmethod
    def ask_date(label: str) -> date:
        raw_value = input(f"{label} date YYYY-MM-DD: ").strip()
        return date.fromisoformat(raw_value)

    @staticmethod
    def ask_decimal(label: str) -> Decimal | None:
        raw_value = input(f"{label}, empty if none: ").strip()

        if raw_value == "":
            return None

        return Decimal(raw_value)

    @staticmethod
    def ask_optional_id(label: str) -> int | None:
        raw_value = input(f"{label}, empty if none: ").strip()

        if raw_value == "":
            return None

        return int(raw_value)

    @staticmethod
    def display_success(message: str) -> None:
        print(message)

    @staticmethod
    def display_error(message: str) -> None:
        print(message)