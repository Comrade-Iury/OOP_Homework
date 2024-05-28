class User:
    def solve(self, n: int):
        pass


class Student(User):
    pass


class Teacher(User):
    def check_solution(self, user: User, n: int):
        pass


class Admin(User):
    def edit(self, n: int):
        pass


class SuperAdmin(Admin):
    def grant(self, user: User):
        pass

