class Car: #First Letter should be capital

    # This is not how attributes are defined
    # brand = None
    # model = None

    # Constructor
    def __init__(self,brand,model): #self -> this => establishing connection with whoever called
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    


# Instance of a class
# my_car has object of class car
my_car = Car("Toyota","Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Tata","Safari")
print(my_new_car.brand)
print(my_car.model)
