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

    def delete_row(self, row):
        self.__table.pop(row)
        self.__rows -= 1

    def delete_col(self, col):
        for r in range(len(self.__table)):
            self.__table[r].pop(col)
        self.__cols -= 1

    def add_row(self, row):
        self.__rows += 1
        self.__table.insert(row, [0] * self.__cols)

    def add_col(self, col):
        self.__cols += 1
        for r in range(len(self.__table)):
            self.__table[r].insert(col, 0)


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

tab.add_row(0)
tab.add_row(2)
tab.add_col(0)
tab.add_col(2)

tab.set_value(0, 0, 2000)
tab.set_value(0, 2, 3000)
tab.set_value(2, 0, 4000)
tab.set_value(2, 2, 5000)

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()