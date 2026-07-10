#Scope

#Local Scope
def my_func():
    my_var = 10
    print(my_var)

my_func()

#Enclosing Scope

#code 1
def outer_func():
    msg = "Hello there!"

    def inner_func():
        print(msg)

    inner_func()

outer_func()

#code 2
def outer_func():
    msg = "Hello there!"
    res = " "

    def inner_func():
        nonlocal res
        res = "How are you?"
        print(msg)

    inner_func()
    print(res)

outer_func()

#Global Scope

#code 1
my_vari = 100

def show_var():
    print(my_vari)

show_var()
print(my_vari)

#code 2
my_var1 = 7

def show_vars():
    global my_var2
    my_var2 = 10
    print(my_var1)
    print(my_var2)

show_vars()

print(my_var2)

#code 3
my_var = 10

def change_var():
    global my_var
    my_var = 20

change_var()
print(my_var)


