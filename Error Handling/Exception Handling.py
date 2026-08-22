try:
    x = 10/0
except ZeroDivisionError:
    print("You can't divide number by 0!")

try:
    x = 10/2
except ZeroDivisionError:
    print("You can't divide by 0!")
else:
    print("Division successful!", x)
finally:
    print("This code always runs!")

try:
    number = int("abc")
    x = 10 / number
except ValueError:
    print("This is an invalid number.")
except ZeroDivisionError:
    print("You can't divide by 0!")
