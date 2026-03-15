# How to keep tack of number of class created

class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        Car.total_car+=1 # for total cars not necessary type counter can handle seperate counter
        # self.total_car +=1 # will not work
        # type(self).total_car += 1
        # This will maintain Seperate conter for all class and nor need to keep inc conter in every class 
        #  just define variable

        if type(self) is not Car:
            type(self).total_car += 1


 # self.total_car +=1 
# Look for total_car in instance
# Not find it
# Use class variable
# But then assign it to instance


class ElectricCar(Car):
    total_car =0
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
        # ElectricCar.total_car+=1


my_kia = Car("Kia","Seltos")
print("Total Car",Car.total_car)
print("Total Car Kia",my_kia.total_car)
my_tesla = ElectricCar("Tesla","Model S","86TY4")
print("Total ElectricCar",ElectricCar.total_car)
print("Total Car Tesla",my_tesla.total_car)


print("Total Car",Car.total_car)

# print(my_tesla.__brand)

