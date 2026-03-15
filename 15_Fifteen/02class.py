# Inheritance

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


my_kia = Car("Kia","Seltos")
print(my_kia.full_name())

my_tesla = ElectricCar("Tesla","Model S","85Khs")
print("car brand",my_tesla.brand)
print("car battery size",my_tesla.battery_size)
print("car Model",my_tesla.model)

print(my_tesla.full_name())