#Numbers and Mathematical Operators
x = 8
y = -3
z = 5
a = 6.478
b = -2.5

print(f"Data type of {x}:",type(x))
print(f"Data type of {y}:",type(y))
print(f"Data type of {a}:",type(a))
print(f"Data type of {b}:",type(b))

#Arithmetic Operators
print(f"Addition of {x} and {y}:",x + y)
print(f"Addition of {a} and {b}:",a + b)
print(f"Addition of {x} and {a}:",x + a)
print(f"Subtract {x} from {y}:",y - x)
print(f"Subtract {b} from {a}:",a - b)
print(f"Subtract {y} from {a}:",a - y)
print(f"Product of {x} and {y}:",x * y)
print(f"Product of {a} and {b}:",a * b)
print(f"Product of {x} and {b}:",x * b)
print(f"Quotient when {x} divided by {y}:",x / y)
print(f"Quotient when {a} divided by {b}:",a / b)
print(f"Quotient when {x} divided by {b}:",x / b)
print(f"Remainder when {x} divided by {y}:",x % y)
print(f"Remainder when {a} divided by {b}:",a % b)
print(f"Floor division of {a} by {b}:",a // b)
print(f"Floor division of {x} by {y}:",x // y)
print(f"{x} to the power {y}:",x ** y)
print(f"{b} to the power {a}:",b ** a)

#Built in functions of int and float
print(f"{x} into float:",float(x))
print(f"{a} into int:",int(a))
print(f"Rounding off {a}:",round(a))
print(f"Rounding off {a} to two digit after decimal:",round(a,2))
print(f"Absolute value of {y}:",abs(y))
print(f"{y} to the power {x}:",pow(y,x))
print(f"{y} to the power {x} whole mod by {z}:",pow(y,x,z))

#Augmented Assignments
var = 10
var += 5
print(var)
var -= 5
print(var)
var *= 2
print(var)
var /= 2
print(var)
var //= 3
print(var)
var %= 4
print(var)
var **= 2
print(var)

my_str = 'hello '
print("My string:",my_str)
my_str *= 4
print("My string 4 times:",my_str)
