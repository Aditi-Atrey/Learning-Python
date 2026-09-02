# Example 1 - getattr()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)

print(getattr(person, "name"))
print(getattr(person, "age"))
print(getattr(person, "city", "Milano"))

attr_name = input("Enter the attribute you want to see: ")
print(getattr(person, attr_name, "Attribute not found"))

# Loop through all attributes of the person object with dir() function
for attr in dir(person):
    # Ignore dunder methods like __init__ or __str__ and regular methods
    if not attr.startswith("__") and not callable(getattr(person, attr)):
        value = getattr(person, attr)
        print(f"{attr}: {value}")

# Example 2 - setattr()
class Configuration:
    pass

# Data loaded at runtime (like from a config or env file)
settings_data = {
    "server_url": "https://api.example.com",
    "timeout_sec": 30,
    "max_reties": 5
    }

config_obj = Configuration()

# Dynamically set attributes using dictionary keys and values
for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url)
print(config_obj.timeout_sec)
