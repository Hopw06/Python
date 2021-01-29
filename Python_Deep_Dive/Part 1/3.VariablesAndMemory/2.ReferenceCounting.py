# Method that returns the reference count for a given variable's memory address:
import ctypes
import sys

def ref_count(address):
    return ctypes.c_long.from_address(address).value

my_var = [1, 2, 3, 4]

print(ref_count(id(my_var)))

# another built-in function:

print(sys.getrefcount(my_var))
# it return 2. Why? because my_var is passed to function, so it will take my_var and store it in other variable. 

other_var = my_var
print(hex(id(my_var)), hex(id(other_var)))
print(ref_count(id(my_var))) # 2

other_var = None
print(ref_count(id(my_var))) # 1