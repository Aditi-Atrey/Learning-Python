#Example 1
class Dog:
    species = "French Bulldog"

    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof woof!"

jack = Dog("Jack")
jill = Dog("Jill")

print(jack.bark())
print(jill.bark())

#Example 2
class Car:
    def __init__(self, colour, model):
        self.colour = colour
        self.model = model

    def describe(self):
        return f"This car is a {self.colour} {self.model}."

car_1 = Car("red", "Toyota Corolla")
car_2 = Car("violet", "Lamborghini Aventador")

print(car_1.describe())
print(car_2.describe())
