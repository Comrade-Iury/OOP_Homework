class SparseArray:
    def __init__(self):
        self.array = [0]

    def __getitem__(self, key):
        if len(self.array) < key + 1:
            self.__setitem__(key, 0)
        return self.array[key]

    def __setitem__(self, key, value):
        if len(self.array) < key+1:
            for _ in range(key - len(self.array)+2):
                self.array.append(0)
        self.array[key] = value

    def __len__(self):
        return len(self.array)


class Polynomial:
    def __init__(self, coefficients: list):
        self.polynom = SparseArray()
        for i in range(len(coefficients)):
            self.polynom[i] = coefficients[i]

    def __call__(self, x):
        res = 0
        for i in range(len(self.polynom)):
            res += self.polynom[i] * (x ** i)
        return res

    def __add__(self, other):
        res = SparseArray()
        for i in range(max(len(self.polynom), len(other.polynom))):
            res[i] = self.polynom[i] + other.polynom[i]
        return Polynomial(res.array)
