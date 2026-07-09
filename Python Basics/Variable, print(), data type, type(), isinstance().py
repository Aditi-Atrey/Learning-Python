#Creating variables and using print function
print("Hello World!")
name = "Aditi"
surname = "Atrey"
age = "17"
print("Name:",name,surname,"Age:",age)

#Common Data Types
int_var = 10
print("Interger:",int_var)
float_var = 6.7
print("Float:",float_var)
str_var = "blue"
print("String:",str_var)
boolean_var = True
print("Boolean:",boolean_var)
set_var = {0.5,4,"apple"}
print("Set:",set_var)
dictionary_var = {"Name":"Aditi","Age":17}
print("Dictionary:",dictionary_var)
tuple_var = (7,"hello",8.5,7)
print("Tuple:",tuple_var)
range_var = range(6)
print("Range:",range_var)
list_var = [1.2,2,"Mango",True,2]
print("List:",list_var)
none_var = None
print("None:",none_var)

#Using type() 
x = "Aditi"
print(type(x))
y = 7
print(type(y))
z = -5.5
print(type(z))
a = True
print(type(a))
b = {0.5,4,"apple"}
print(type(b))
c = {"Name":"Aditi","Country":"India"}
print(type(c))
d = (7.8,4,"orange")
print(type(d))
e = range(8)
print(type(e))
f = [1.8,2,9,True,"Yes"]
print(type(f))
g = None
print(type(g))

#Using isinstance()
p = "12"
print("Is it an integer:",isinstance(p,int))
q = 12
print("Is it an integer or a float:",isinstance(q,(int,float)))
r = 1.6
print("Is it an integer or/and a float:",isinstance(r,(int,float)))

