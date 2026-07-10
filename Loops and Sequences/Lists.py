#Lists

cities = ["Nagpur", "Mumbai", "Pune"]
print(cities[0])
print(cities[-1])

name = "Aditi"
print(list(name))
print(len(name))

cities[1] = "Delhi"
print(cities)

del cities[0]
print(cities)

print("Mumbai" in cities)

developer = ["Alice", 25, ["Python", "Rust", "C++"]]
print(developer[2])
print(developer[2][1])

new_developer = ["Alice", 35, "Rust developer"]
new_name, age, job = new_developer
print(new_name)
print(age)
print(job)

grocery = ["Mango", "Ladyfinger", "Umbrella"]
fruit, *rest = grocery
print(fruit)
print(rest)

colours = ["black", "purple", "pink","blue"]
print(colours[:3])

numbers = [1, 2, 3, 4, 5, 6]
print(numbers[1::2])
