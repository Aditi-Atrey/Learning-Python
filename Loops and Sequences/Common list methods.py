#Common list methods

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

even_numbers = [8, 10]
numbers.append(even_numbers)
print(numbers)

odd_numbers = [11, 13]
numbers.extend(odd_numbers)
print(numbers)

numbers.insert(3, 2.5)
print(numbers)

numbers.remove(4)
print(numbers)

numbers.pop(5)
print(numbers)

numbers.clear()
print(numbers)

cricketers = ["virat kohli", "rohit sharma", "kl rahul", "jasprit bumrah", "ms dhoni"]
cricketers.sort()
print(cricketers)

cricketers.reverse()
print(cricketers)

print(cricketers.index("kl rahul"))
