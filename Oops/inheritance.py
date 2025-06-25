""" we have done inheritance and encaplslation of
variable brand by putting __ to make it private and have implemented 
get method so that it can be accessed
"""
class Car:
    def __init__(self,brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"

    def display(self):
        print("Car Brand =",self.__brand)
        print("Car Model =",self.model)

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def display(self):
        super().display()
        print("Car Battery Size =",self.battery_size)

my_ec_car=ElectricCar("Tesla","Model S","85kwh")
my_ec_car.display()
#print(my_ec_car.brand)
print(my_ec_car.get_brand())

print("Instance or nott =",isinstance(my_ec_car,Car))
        