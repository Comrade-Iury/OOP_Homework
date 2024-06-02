from abc import ABC, abstractmethod


class CarFactory:
    @abstractmethod
    def produce_car(self):
        pass


class ElectricCarFactory(CarFactory):
    def produce_car(self):
        return ElectricCar()


class PetrolCarFactory(CarFactory):
    def produce_car(self):
        return PetrolCar()


class HybridCarFactory(CarFactory):
    def produce_car(self):
        return HybridCar()


class Car:
    def __init__(self):
        pass

    @abstractmethod
    def drive(self):
        return ""


class ElectricCar(Car):
    def __init__(self):
        super().__init__()
        self.engine_power = 100
        self.fuel_consumption = 200

    def drive(self):
        return "Driving an electric car"


class PetrolCar(Car):
    def __init__(self):
        super().__init__()
        self.engine_power = 90
        self.fuel_consumption = 100

    def drive(self):
        return "Driving a petrol car"


class HybridCar(Car):
    def __init__(self):
        super().__init__()
        self.engine_power = 120
        self.fuel_consumption = 180

    def drive(self):
        return "Driving a hybrid car"



