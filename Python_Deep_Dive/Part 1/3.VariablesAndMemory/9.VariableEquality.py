# a and b share the same memory address.
a = 10
b = 10

print("a, b = ", a, b)
print(hex(id(a)))
print(hex(id(b)))

print("a is b", a is b)
print("a == b", a == b)

# But for list, it does not same.
a = [1, 2, 3]
b = [1, 2, 3]

print(hex(id(a)))
print(hex(id(b)))

print("a is b", a is b)
print("a == b", a == b)

# Python will attempt to compare values as best as possible, for example:
a = 10
b = 10.0

print(type(a)) # int
print(type(b)) # float

print('a is b: ', a is b)
print('a == b: ', a == b) # so even different type, a and b are equal.

# Same
c = 10 + 0j
print(type(c))

print('a is c', a is c)
print('a == c: ', a == c)
################################################################################################
##################### The None object ##########################################################

# None is a built-in variable of type NoneType.
# NoneType object are immutable. So Python's memory manager will therefore use shared references to the None object.
# It's mean that all None objects has same memory address or have only one None object.

print(type(None))
print(hex(id(None)))

a = 6
print(hex(id(a)))

a = None
print(hex(id(a))) # same memory address with None object.

print(a is None)
