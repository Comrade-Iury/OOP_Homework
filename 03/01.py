class FoodInfo:
    def __init__(self, proteins: int, fats: int, carbohydrates: int):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def get_proteins(self):
        return self.proteins

    def get_fats(self):
        return self.fats

    def get_carbohydrates(self):
        return self.carbohydrates

    def get_kcalories(self):
        return self.proteins * 4 + self.fats * 9 + self.carbohydrates * 4

    def __add__(self, other):
        proteins = self.proteins + other.proteins
        fats = self.fats + other.fats
        carbohydrates = self.carbohydrates + other.carbohydrates
        return FoodInfo(proteins, fats, carbohydrates)

