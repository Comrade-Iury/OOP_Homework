class SparseArray:
    def __init__(self):
        self. array = [0]

    def __getitem__(self, key):
        if len(self.array) < key + 1:
            self.__setitem__(key, 0)
        return self.array[key]

    def __setitem__(self, key, value):
        if len(self.array) < key+1:
            for _ in range(key - len(self.array)+2):
                self.array.append(0)
        self.array[key] = value

