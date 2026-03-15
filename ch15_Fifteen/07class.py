# Proprty Decorator =>make model attribute read only 

class Car:
    def __init__(self,model,brand):
        self.__model = model
        self.__brand = brand

    @property
    def model_func(self):
        return self.__model
    

class Electric:
    def __init__(self,battery_size):
        self.__battery_size = battery_size

    def battery(self):
        return self.__battery_size
    @property
    def battery_func(self):
        print("Logs")
        return self.__battery_size.upper()
    
my_car = Car("KS","fs")
print(my_car.model_func)

my_car.brand = "5"
my_car.model = "5"

# This creates a new attribute __model not __Car__model
my_car.__brand = "5R"
my_car.__model = "5R"
print(my_car.__model )
print(my_car.__brand )

print(my_car.model_func)
print(my_car.__dict__)

        
my_tesla = Electric("700errr")
print(my_tesla.battery())
print(my_tesla.battery_func)