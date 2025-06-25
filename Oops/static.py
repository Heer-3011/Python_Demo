#static method can be can accesed by the class itself and not its object 

class Person:
    count=0
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        Person.count+= 1

    def display(self):
        print(self.name , self.age , self.gender)
    
    #implementation of the static method in python with no self argument required in it 
    @staticmethod
    def general_des():
        return "Person are living things"


person_1=Person("Heer","20","Female")
person_2=Person("Shobhna","43","Female")
person_3=Person("Meet","24","Male")
person_1.display()
#print(person_1.general_des())
print(Person.general_des())
