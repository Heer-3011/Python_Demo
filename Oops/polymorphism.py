class Car:
    total_car=0
    def __init__(self,brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car +=1

    def get_brand(self):
        return self.__brand + "!"

    def fuel_type(self):
        return "Petrol or disele"

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

    def fuel_type(self):
        return "Electic charge"

my_ec_car=ElectricCar("Tesla","Model S","85kwh")
my_car2=Car("Suzuki","Swift")
my_thar=Car("honda","thar")
my_nexon=Car("Tata","Nexon") 

print(Car.total_car)
print(my_car2.fuel_type())
print(my_ec_car.fuel_type())