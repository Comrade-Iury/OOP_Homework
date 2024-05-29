class Profile:
    def __init__(self, profession: str):
        self.profession = profession

    def info(self):
        return ""

    def describe(self):
        print(f"Специальность: {self.profession},  {self.info()}")


class Vacancy(Profile):
    def __init__(self, profession: str, salary: float):
        super().__init__(profession)
        self.salary = salary

    def info(self):
        return f"Предполагаемая зарплата: {self.salary}"


class Resume(Profile):
    def __init__(self, profession: str, experience: float):
        super().__init__(profession)
        self.experience = experience

    def info(self):
        return f"Стаж работы: {self.experience}"


worker = Resume("builder", 12)
worker.describe()

company = Vacancy("builder", 30000)
company.describe()