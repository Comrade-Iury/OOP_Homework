class ReversedList:
    def __init__(self, lst: list):
        self.lst = lst
        lst1 = self.lst.copy()
        for i in range(len(lst1)):
            self.lst[i] = lst1[-(i+1)]
        lst1.clear()

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, key):
        return self.lst[key]

