class Selector:
    def __init__(self, all_numbers: list):
        self.__all_numbers = all_numbers

    def get_odds(self):
        return filter(lambda n: n % 2, self.__all_numbers)

    def get_evens(self):
        return filter(lambda n: not n % 2, self.__all_numbers)
