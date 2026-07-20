#Dictionary

pizza = {
    "name": "Margherita Pizza",
    "price": 8.9,
    "calories_per_slice": 250,
    "toppings": ["Mozzarella", "Basil"]
    }

burger = dict([("bread_type", "Bun"), ("price", 15), ("vegies", "Lettuce")])

#Bracket Notation

print(pizza["name"])
pizza["name"] = "Margherita"
print(pizza["name"])

#Common Dictionary Methods

print(burger.get("bread_type", "Pav"))
print(pizza.keys())
print(burger.values())
print(pizza.items())
print(burger.clear())
print(pizza.pop("calories_per_slice", 150))
print(pizza.popitem())
print(pizza.update({"price": 20, "total_time": 25}))
print(pizza.items())
print(burger.items())

