class Summator:
    def __init__(self, n=1):
        self.n = n

    def transform(self, num):
        return num

    def sum(self, n):
        res = 0
        for i in range(n + 1):
            res += self.transform(i)
        return res


class PowerSummator(Summator):
    def __init__(self, power):
        super().__init__()
        self.power = power

    def transform(self, num):
        return num ** self.power


class SquareSummator(PowerSummator):
    def __init__(self, power=2):
        super().__init__(power)


class CubeSummator(PowerSummator):
    def __init__(self, power=3):
        super().__init__(power)
