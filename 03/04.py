class Date:
    CALENDAR = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, month: int, day: int):
        days = 0
        for i in range(month):
            if i+1 == month:
                days += day
            else:
                days += self.CALENDAR[i+1]

        self.days = days

    def __sub__(self, other):
        return self.days - other.days
