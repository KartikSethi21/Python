class Car:
    def __init__(self,brand,model):
        self.__brand = brand # to make brand private
        self.model = model
    # getter method
    def get_brand(self):
        return self.__brand + '!'
    
    def set_name(self,brand):
        self.__brand = brand
        # self._Car__brand # inside how it looks

    def full_name(self):
        return f"{self.__brand} {self.model}"


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    # will work but no need
    # def set_name(self,brand):
    #     super().set_name(brand)



my_kia = Car("Kia","Seltos")
print(my_kia.full_name())
my_kia.set_name("XUV700")
print(my_kia.full_name())
my_tesla = ElectricCar("Tesla","Model S","86TY4")
# print(my_tesla.__brand)
print(my_tesla.get_brand())
my_tesla.set_name("Ferr")
print(my_tesla.full_name())

        