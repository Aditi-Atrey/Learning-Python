#Enumerate()

languages = ["Spanish", "English", "Russian", "Chinese"]

#Method 1 (not by enumerate())

index = 0

for language in languages:
    print(f"Index {index} and Language {language}")
    index += 1

#Method 2

print(list(enumerate(languages)))

#Method 3

for index, language in enumerate(languages):
    print(f"Index {index} and Language {language}")

#Method 4 with index change

for index, language in enumerate(languages, 1):
    print(f"Index {index} and Language {language}")
