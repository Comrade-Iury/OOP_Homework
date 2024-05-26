class SquareFunction:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return (x ** 2) * self.a + x * self.b + self.c
# Ваш код

sf = SquareFunction(0, 0, 1)
print(sf(-2))
print(sf(-1))
print(sf(-0))
print(sf(1))
print(sf(2))
print(sf(10))