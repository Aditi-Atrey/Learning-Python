#List Functions

#1. filter()

words = ["tree", "sun", "mountain", "sky", "cloud", "river"]

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words)

#2. map()

celcius = [0, 10, 20, 30, 40]

def to_fahreinheit(temp):
    return (temp * 9/5) + 32

fahreinheit = list(map(to_fahreinheit, celcius))
print(fahreinheit)

#3. sum()

numbers = [5, 10, 15, 20]

total_1 = sum(numbers)
print(total_1)

total_2 = sum(numbers, 30)
print(total_2)

total_3 = sum(numbers, start = 30)
print(total_3)
