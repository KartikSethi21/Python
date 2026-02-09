# Inheritance

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        print(f"{self.brand} {self.model}")


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        pass
        