#Booleans and Conditional

#Comparison Operators
print(3 == 4)
print(3 != 4)
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)

#If statement
age1 = 19
if age1 >= 18:
    print("You are an adult.")

age2 = 15
if age2 >= 18:
    print("You are an adult.")

#If...else statement
age3 = 15
if age3 >= 18:
    print("You are an adult.")
else:
    print("You are not an adult yet.")

#Elif statement
age4 = 12
if age4 >= 60:
    print("You are a senior citizen.")
elif age4 >= 30:
    print("You are an adult in your prime.")
elif age4 >= 18:
    print("You are a young adult.")
elif age4 >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

#Nested conditional statement
is_citizen1 = True
age5 = 25

if is_citizen1:
    if age5 >= 18:
        print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#Truthy and falsy values
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(True))
print(bool("Hello"))
print(bool(45))
print(bool("False"))
print(bool(""))

#Boolean/Logical Operator

#1. and operator
is_citizen2 = True
age6 = 25
print(is_citizen2 and age6)

if is_citizen2 and age6 >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#2. or operator
age7 = 19
is_employed = False
print(age7 or is_employed)

is_student = True
if is_student or age7 < 18:
    print("You are eligible for student discount.")
else:
    print("You are not eligible for student discount.")

#3. not operator
print(not "")
print(not True)
print(not 0)
print(not "Hello")
print(not 1)
print(not False)

is_admin = False
if not is_admin:
    print("Access denied for non-administrators.")
else:
    print("Welcome, administrator!")


