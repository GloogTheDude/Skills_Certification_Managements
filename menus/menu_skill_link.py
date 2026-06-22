class MenuSkillLink():

    @staticmethod
    def ask_skill_levels() -> list[tuple[int, int]]:
        skill_levels = []

        while True:
            raw_id = input("Skill id, empty to stop: ").strip()

            if raw_id == "":
                break

            id_skill = int(raw_id)
            level = int(input("Level: "))

            skill_levels.append((id_skill, level))

        return skill_levels