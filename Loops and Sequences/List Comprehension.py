#List Comprehension

even_num = []

for num in range(21):
    if num % 2 == 0:
        even_num.append(num)

print(even_num)

#Above example by list comprehension

even_num = [num for num in range(21) if num % 2 == 0]
print(even_num)

#Example 2

numbers = [1, 2, 3, 4, 5, 6]
result = [(number, "Even") if number % 2 == 0 else (number, "Odd") for number in numbers]
print(result)
