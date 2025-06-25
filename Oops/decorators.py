#make age read-only variable
class Person:
    count=0
    def __init__(self,name,age,gender):
        self.name=name
        self.__age=age
        self.gender=gender
        Person.count+= 1

    def display(self):
        print(self.name , self.age , self.gender)
    
    #we have to give aaccess of variable through function and not to manipulate it we can use following
    #no manipulation should be there 
    @property
    def age(self):
        return self.__age

person1=Person("heer","20","female")

#person1.age=23
print(person1.age)

    