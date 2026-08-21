#Using print() and f - strings
def add(a,b):
    result = a + b
    print(f"Adding {a} and {b} gives {result}.")
    return result

#pdb Module
import pdb

def divide(a,b):
    pdb.set_trace()
    return a/b

print(divide(10,2))

