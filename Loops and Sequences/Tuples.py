#Tuples

numbers = (1, 2, 3, 4, 5, 6)
print(numbers[0])
print(numbers[-2])

name = "Aditi"
print(tuple(name))

cities = ("Nagpur", "Pune", "Mumbai", "Lucknow","Delhi")
print("Pune" in cities)

developer = ("B.Tech", 34, "Rust developer")
education, age, job = developer
print(education)
print(age)
print(job)

grocery = ("Mango", "Potato", "Seeds")
fruit, *rest = grocery
print(fruit)
print(rest)

print(numbers[2:5])
print(numbers[0::2])
