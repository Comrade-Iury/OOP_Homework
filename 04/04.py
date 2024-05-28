class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, user, message: str):
        pass

    def post(self, message):
        pass

    def info(self):
        return ""

    def describe(self):
        print(self.info())


class Person(User):
    def __init__(self, name, birth_date):
        super().__init__(name)
        self.birth_date = birth_date

    def info(self):
        return f"Дата рождения: {self.birth_date}"

    def subscribe(self, user: User):
        pass


class Community(User):
    def __init__(self, name: str, description: str):
        super().__init__(name)
        self.description = description

    def info(self):
        return f"Описание: {self.description}"

