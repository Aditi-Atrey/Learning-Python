#Sets

my_set = {1, 2, 3, 4, 5}
empty_set = set()

print(empty_set)

my_set.add(6)
print(my_set)
my_set.remove(4)
print(my_set)
my_set.discard(5)
print(my_set)
my_set.discard(8)
print(my_set)
my_set.clear()
print(my_set)

new_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(new_set.issubset(your_set))
print(new_set.issuperset(your_set))
print(new_set.isdisjoint(your_set))

print(new_set | your_set)
print(new_set & your_set)
print(new_set - your_set)
print(new_set ^ your_set)

new_set |= your_set
print(new_set)

print(5 in new_set)
