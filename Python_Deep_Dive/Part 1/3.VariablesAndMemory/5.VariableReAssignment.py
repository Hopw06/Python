# NOTICE HOW THE MEMORY ADDRESS OF a IS DIFFERENT EVERY TIME.
a = 10
print(hex(id(a)))

a = 15
print(hex(id(a)))

a = 5
print(hex(id(a)))

a = a + 1
print(hex(id(a)))

# however, look at this:
a = 10
b = 10
print(hex(id(a)))
print(hex(id(b)))

# address of a and b is same.