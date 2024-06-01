from abc import ABC, abstractmethod


class Animal:
    @abstractmethod
    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return "Рычание!"


class Monkey(Animal):
    def make_sound(self):
        return "Визг!"


class Elephant(Animal):
    def make_sound(self):
        return "Трубление!"


class AnimalFactory:
    @abstractmethod
    def create_animal(self):
        pass


class LionFactory(AnimalFactory):
    def create_animal(self):
        return Lion


class MonkeyFactory(AnimalFactory):
    def create_animal(self):
        return Monkey


class ElephantFactory(AnimalFactory):
    def create_animal(self):
        return Elephant


def interact_with_animal(factory):
    animal = factory.create_animal()
    print(animal.make_sound(animal))

