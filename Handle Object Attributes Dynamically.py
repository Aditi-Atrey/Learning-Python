#Example 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)

print(getattr(person, "name"))
print(getattr(person, "age"))
print(getattr(person, "city", "Milano"))
