# Write program to test Garbage collection in Python.
import ctypes
import gc

# function return reference counts.
def ref_count(address):
    return ctypes.c_long.from_address(address).value

# funtion to find object with given address.
def object_by_id(address):
    for obj in gc.get_objects():
        if id(obj) == address:
            return "Object found"
    return "Not found"

# Create two class A, B to test reference circular.
class A:
    def __init__(self):
        self.b = B(self)
        print("A: self: {0}, b: {1}".format(hex(id(self)), hex(id(self.b))))

class B:
    def __init__(self, a):
        self.a = a
        print("B: self: {0}, a: {1}".format(hex(id(self)), hex(id(self.a))))

gc.disable() # disable garbage collection

my_var = A()

a_id = id(my_var)
b_id = id(my_var.b)

print('refcount(a) = {0}'.format(ref_count(a_id))) # 2 my_var, b.a
print('refcount(b) = {0}'.format(ref_count(b_id))) # 1 a.b

print('a: {0}'.format(object_by_id(a_id)))
print('b: {0}'.format(object_by_id(b_id)))

# reset my_var reference
my_var = None
print('refcount(a) = {0}'.format(ref_count(a_id))) # 1 b.a
print('refcount(b) = {0}'.format(ref_count(b_id))) # 1 a.b

print('a: {0}'.format(object_by_id(a_id)))
print('b: {0}'.format(object_by_id(b_id)))
# => it's still has a reference to A object in B object. (b.a)

# But now we can not point to a.b to reset reference of A or a.b.a to reset reference of B.
# Because my_var is None now => leak memory

# Turn on garbage collection and test again.
gc.collect()
print('refcount(a) = {0}'.format(ref_count(a_id))) # 1 b.a
print('refcount(b) = {0}'.format(ref_count(b_id))) # 1 a.b

print('a: {0}'.format(object_by_id(a_id)))
print('b: {0}'.format(object_by_id(b_id)))