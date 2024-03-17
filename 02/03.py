class AmericanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, num: int):
        self.year = num

    def set_month(self, num: int):
        self.month = num

    def set_day(self, num: int):
        self.day = num

    def format(self):
        if self.day < 10:
            self.day = "0" + str(self.day)
        if self.month < 10:
            self.month = "0" + str(self.month)
        return f"{self.month}.{self.day}.{self.year}"


class EuropeanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, num: int):
        self.year = num

    def set_month(self, num: int):
        self.month = num

    def set_day(self, num: int):
        self.day = num

    def format(self):
        if self.day < 10:
            self.day = "0" + str(self.day)
        if self.month < 10:
            self.month = "0" + str(self.month)
        return f"{self.day}.{self.month}.{self.year}"

