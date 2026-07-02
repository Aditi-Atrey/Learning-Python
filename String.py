#Strings

#Multiline strings
print("Hello world, how are you?")
print("""Hello world
How are you?""")

#In operator, len() and indexing
name='Aditi Atrey'
age='17'
print("Is Aditi in name:",'Aditi' in name)
print("Length of Aditi Atrey is ",len(name))
print("The index no. 0 is of character",name[0])
print("The index no. 7 is of character",name[7])
print("The index no. -7 , i.e. 7 from back is of character",name[-7])

#Concatenation 
str1='Hi'
str2='Friend'
str3=str1+' '+str2
print("The concatenation of Hi and Friend is",str3)
name_age=name+' '+str(age)
print("The concatenation of name and age is",name_age)

#Augmented concatenation operator
x='alpha '
y='beta'
z=x
z+=y   
print(z)

#Interpolation
name_and_age=f"My name is {name} and I am {age} years old."
print(name_and_age)
a=7
b=9
sum_of_numbers=f"Sum of {a} and {b} is {a+b}."
print(sum_of_numbers)

#String Slicing
print(name[1:4])
print(name[:7])
print(name[2:])
print(name[:11:2])
print(name[::-1])

#Common String Methods
new_name1=name.upper()
print("My name in uppercase:",new_name1)
new_name2=name.lower()
print("My name in lowercase:",new_name2)
new_name3=name.strip()
print(new_name3)
new_name4=name.replace('Aditi','Ojas')
print("Replacing Aditi by Ojas:",new_name4)
new_name5=name.split()
print(new_name5)
my_list=["hello","world"]
joined_str=' '.join(my_list)
print(joined_str)
print("My name start with Aditi:",name.startswith('Aditi'))
print("My name end with Aditi:",name.endswith('Aditi'))
print(name.find('Atrey'))
print(name.find('Ojas'))
print(name.count('i'))
print(name.count('t'))
print("My name capitalized:",name.capitalize())
print("Is my name in uppercase:",name.isupper())
print("Is my name in lowercase:",name.islower())
print("Capitalizing first letter of ech word of my name:",name.title())





