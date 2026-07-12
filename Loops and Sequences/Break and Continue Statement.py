#Statement - break

names = ["Jess", "Naomi", "Tim"]

for name in names:
    if name == "Naomi":
        break
    print(name)


#Statement - continue

for name in names:
    if name == "Naomi":
        continue
    print(name)


#Statement in nested for loop

words = ["sky", "apple", "rythm", "fly", "orange"]

for word in words:
    for letter in word:
        if letter.lower() in "aeiou":
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
            print(f"'{word}' has no vowel")
        

    
        
