class MinStat:
    def __init__(self):
        self.sequence = list()

    def add_number(self, num: int):
        self.sequence.append(num)

    def result(self) -> int:
        if self.sequence:
            return min(self.sequence)
        return None


class MaxStat:
    def __init__(self):
        self.sequence = list()

    def add_number(self, num: int):
        self.sequence.append(num)

    def result(self) -> int:
        if self.sequence:
            return max(self.sequence)
        return None


class AverageStat:
    def __init__(self):
        self.sequence = list()

    def add_number(self, num: int):
        self.sequence.append(num)

    def result(self) -> float:
        if self.sequence:
            return sum(self.sequence) / len(self.sequence)
        return None
