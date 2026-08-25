#Example 1
class Dog:
    species = "French Bulldog"   #Class Attribute

    def __init__(self, name):
        self.name = name         #Instance Attribute

print(Dog.species)

dog1 = Dog("Jack")
print(dog1.species)
print(dog1.name)

dog2 = Dog("Tom")
print(dog2.species)
print(dog2.name)

#Example 2
class Car:
    def __init__(self, colour, model):
        self.colour = colour
        self.model = model

car1 = Car("Yellow", "Mercedes G Wagon")
car2 = Car("Violet", "Lamborghini Aventador")

print(car1.colour)
print(car2.colour)

print(car1.model)
print(car2.model)

    
