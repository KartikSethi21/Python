# Multiple Inheritance

class Battery:
    def battery_info(self):
        return "This is battery"
    
class Engine:
    def engine_info(self):
        return "This is engine"

class Car:
    def my_car(self):
        pass

class ElectricCar(Battery,Engine,Car):
    pass


my_new_tesla = ElectricCar()
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())