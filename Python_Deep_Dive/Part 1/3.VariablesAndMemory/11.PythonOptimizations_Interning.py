a = 10
b = 10

# same memory address
print(hex(id(a)))
print(hex(id(b)))

# Python pre cache integer object in range [-5, 256]
# So with variable refer to value in this range, will have same memory address.

a = 257
b = 257

print(hex(id(a)))
print(hex(id(b)))
print(a is b)

# but it is still same memory address, a is b. Why?
# Because The Python Parser will analyze the source file and find out there are variables refer to same value.
# So it will create only one object and make these variables point to it.

# You only can test pre cache integer object in range [-5, 256] by typing each line in Python shell. 

# It work same with float object

a = 5.0
b = 5.0

print(hex(id(a)))
print(hex(id(b)))
print(a is b)

# or even differnt kind of express the value
a = 10
b = 0b1010
c = 0xA

print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))

print(a is b)
print(b is c)

# Ofcourse, it only works for imutable object.