class Table:
    def __init__(self, rows: int, cols: int):
        self.__rows = rows
        self.__cols = cols
        self.__table = list()
        for r in range(rows):
            self.__table.append(list())
            for c in range(cols):
                self.__table[r].append(0)

    def get_value(self, row, col):
        if 0 <= row < self.__rows and 0 <= col < self.__cols :
            return self.__table[row][col]
        return None

    def set_value(self, row: int, col: int, value: int):
        self.__table[row][col] = value

    def n_rows(self):
        return self.__rows

    def n_cols(self):
        return self.__cols


tab = Table(1, 1)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.set_value(0, 0, 1000)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()