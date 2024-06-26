class Summator:
    def __init__(self, n):
        self.n = n
        self.power = 1

    def transform(self):
        self.n = self.n

    def sum(self):
        res = 0
        for i in range(self.n + 1):
            res += i ** self.power
        return res


class SquareSummator(Summator):
    def transform(self):
        self.power = 2


class CubeSummator(Summator):
    def transform(self):
        self.power = 3


a = Summator(10)
a.transform()
print(a.sum())

b = SquareSummator(10)
b.transform()
print(b.sum())

c = CubeSummator(10)
c.transform()
print(c.sum())