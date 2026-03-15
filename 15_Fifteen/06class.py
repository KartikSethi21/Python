# Static Method => belongs to class instead of instance of class
# Ther are 3 types of methods
# 1> Instance method in class that uses self => Uses instance data
# 2> Class Method used in class that uses cls => @classmethod uses Uses class data
# #> Static method uses neither class or instance data =>  @staticmethod Just utility function
class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_car += 1
        # type(self).total_car+=1
        # self.__class__.total_car+=1

    @classmethod
    def get_total_cars(cls):
        return cls.total_car
    

    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
# This method belongs to the class
# It does NOT use self
# It does NOT use cls
# It behaves like a normal function
# It is just placed inside the class for logical grouping
# It has no access to instance data.


# Factory Method Alternative to Constructor

class Newcar:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    @classmethod
    def fromStr(cls,data_str):
        brand,model = data_str.split("-")
        return cls(brand,model)
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    # Here cls is class name basically calling Newcar(brand,model)
    # “Create an object of whatever class called this method.”

class Electric(Newcar):
    def __init__(self,brand,model):
        super().__init__(brand,model)



print(Car.get_total_cars())


my_car = Car("Honda","Desire")
print(my_car.general_description())
print(Car.general_description())
print(Car.get_total_cars())


my_car = Newcar.fromStr("Honda-Desire")
print(my_car.full_name())
my_elec = Electric.fromStr("Tesla-XCVB9")
print(my_elec.full_name())

        