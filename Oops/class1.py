class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Car Brand =",self.brand)
        print("Car Model =",self.model)

my_car=Car("Toyoto","Corolla")  
print(my_car.brand)
print(my_car.model)

my_car2=Car("Suzuki","Swift")

my_car.display()
my_car2.display()
