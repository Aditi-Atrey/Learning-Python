#Zip()

developers = ["Naomi", "Dario", "Jessica", "Tom"]
ids = [1, 2, 3, 4]

#Method 1

print(list(zip(developers, ids)))

#Method 2

for name, id in zip(developers, ids):
    print(f"Name: {name}")
    print(f"ID: {id}")
