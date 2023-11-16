class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        
class Cake:
    def __int__(self,cake_flavor,cake_frosting):
        self.cake_flavor = cake_flavor
        self.cake_frosting = cake_frosting
     #can you fill out the rest of this for me? im dumb
    #the cake needs to have the cake flavor and cake frosting stored

class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length
        
        
    def breedGuess(self):
        if self.fur_length == "long":
            return("Domestic Longhair")
        else:
            return("Domestic Shorthair")
            
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        
    #create your own function! what do you want it to do?
class shoes:
    def __init__(self, brand, size, color):
        self.size = size
        self.brand = brand
        self.color = color
   
def main():
    #fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    dog1 = Dog("draco","4")
    print(dog1.name, dog1.age)

    #and what about a new employee
    Employee1 = Employee("john","28", "accounting")
    #how would we print out each of the variables from newEmployee?
    print(Employee1.name, Employee1.idNumber, Employee1.department)
    
    #now create and print out a cake you make

    
    
    #and now create another cake and print it out
    
    
    
    #create a cat!
    cat1 = Cat("mike","5","long")
    #create another cat!
    cat2 = Cat("kyle","3","short")
    #What would we put here to print out the result of breedGuess for cat1?
    print(cat1.name, cat1.age, cat1.fur_length)
    print(cat2.name, cat2.age, cat1.fur_length)
    #create a car!
    car1 = Car("porsche", "2013", "green")
    #Now print out the function you made for car :)
    print(car1.model, car1.year, car1.color)
main()
