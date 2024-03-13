class Balance:
    def __init__(self):
        self.__right_mass = 0
        self.__left_mass = 0

    def add_right(self, mass):
        self.__right_mass += mass

    def add_left(self, mass):
        self.__left_mass += mass

    def result(self):
        if self.__left_mass < self.__right_mass:
            return "R"
        if self.__left_mass > self.__right_mass:
            return "L"
        return "="


balance = Balance()
balance.add_right(10)
balance.add_left(5)
balance.add_left(5)
print(balance.result())
balance.add_left(1)
print(balance.result())