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

    
