# isinstance

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model=model
    
    def fuel_type(self):
        return "Petrol or Diesel"
    


class ElectricCar(Car):
    def __init__(self,brand,model,batter_size):
        super().__init__(brand,model)
        self.batter_size = batter_size

    def fuel_type(self):
        return "Electric Car"
    


safari = Car("HONDA","Desire")
print(safari.fuel_type())

my_tesla = ElectricCar("Tes","XUV$0","37u")
print(my_tesla.fuel_type())



print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))


print(isinstance(safari,ElectricCar))