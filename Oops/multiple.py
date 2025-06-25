class Engine:
    def engine_info(self):
        return "This is engine of the car"
class Car:
    total_car=0
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    def display(self):
        print("Model=",self.model)
        print("Bramd=",self.brand)
   
class Battery:
    def battery(self):
        return "This is Battery of the car"
    
class ElectricCarrTest(Engine,Battery,Car):
    pass

car1=ElectricCarrTest("Tesla","Model S")
car1.display()

print(car1.engine_info())
print(car1.battery())