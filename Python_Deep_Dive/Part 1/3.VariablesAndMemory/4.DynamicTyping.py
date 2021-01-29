# Python is dynamically typed.
# A variable is simply the type of the object the variable name points to (references).
# The variable itself has no associated type.

a = "hello"

print(type(a))

a = 10

print(type(a))


a = lambda x: x**2

print(a(2))

print(type(a))

# The type of a variable is changed over time, in fact it was simply the type of the object a was referencing at that time. 
# NO TYPE WAS EVER ATTACHED TO THE VARIABLE NAME IFSELF.