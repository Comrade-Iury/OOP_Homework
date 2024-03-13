class OddEvenSeparator:
    def __init__(self):
        self.__odds = list()
        self.__evens = list()

    def add_number(self, num: int):
        if num % 2:
            self.__odds.append(num)
        else:
            self.__evens.append(num)

    def even(self):
        return self.__evens

    def odd(self):
        return self.__odds
