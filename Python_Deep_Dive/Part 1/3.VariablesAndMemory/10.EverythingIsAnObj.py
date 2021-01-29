a = 10
# a is an object of type int, i.e. a is an instance of int class
print(type(a))

b = int(10)
print(b)
print(type(b))

# we can even request the class documentation:
# help(int)

# We can create a number base 2
# such as:
c = int('10', 2)
print(c)
print(type(c))

# Function are object too
def square(a):
    return a ** 2

print(type(square))

# we can assign function to a variable
f = square

print(type(f))
print(f(2))
print(f is square)

# A function can return a function
def cube(a):
    return a ** 3

def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube

f = select_function(1)
print(hex(id(f)))
print(hex(id(square)))
print(hex(id(cube)))

print(type(f))
print('f is square: ', f is square)
print('f is cube: ', f is cube)
print(f)
print(f(2))

# we could even call this way
print(select_function(1)(5))

# A function can be passed as an argument to another function.
def exec_function(fn, n):
    return fn(n)

print(exec_function(cube, 2))