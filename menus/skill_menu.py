from dto.skill_dto import SkillCrudDTO
from models.skill import Skill


class SkillMenu:
    @staticmethod
    def main_menu() -> int:
        user_choice = -1

        while not (0 <= user_choice <= 4):
            print("===== SKILL CRUD =====")
            print("1. List skills")
            print("2. Create skill")
            print("3. Update skill")
            print("4. Delete skill")
            print("0. Leave")

            user_choice = int(input("Your choice: "))

        return user_choice
    @staticmethod
    def display_skills(skills: list[SkillCrudDTO]) -> None:
        print("===== SKILLS =====")

        if not skills:
            print("No skill found.")
            return

        for skill in skills:
            domaine_name = skill.domaine_name or "No domain"
            print(f"{skill.id_skill}: {skill.name_skill} - {domaine_name}")

    @staticmethod
    def ask_name_skill() -> str:
        return input("Skill name: ").strip()

    @staticmethod
    def ask_id_skill() -> int:
        return int(input("Skill id: "))

    @staticmethod
    def ask_id_domaine() -> int | None:
        raw_value = input("Domaine id, empty if none: ").strip()

        if raw_value == "":
            return None

        return int(raw_value)

    @staticmethod
    def display_success(message: str) -> None:
        print(message)

    @staticmethod
    def display_error(message: str) -> None:
        print(message)