# In Python the global scope refers to the module scope.
a = 10 # a is the global variable

def my_func(n):
    print('global:', a) # a is the global variable
    c = a ** n
    return c # n, c is local in function my_func

print(my_func(2))

# But remember that the scope of a variable is determined by where it is assigned. In particular, any variable defined (i.e. assigned a value) inside a function is local to that function, even if the variable name happens to be global too!

def my_func(n):
    a = 2
    print("a local in my_func", a)
    c = a ** 2
    return c

print("Global:", a)
print(my_func(3))
print("Global: ", a)


# In order to change the value of a global variable within an inner scope, we can use the global keyword as follows:
def my_func(n):
    global a
    a = 2
    c = a ** 2
    return c

print("Global:", a)
print(my_func(3))
print("Global: ", a) # the value of a will be changed.

# In fact, we can create global variables from within an inner function - Python will simply create the variable and place it in the global scope instead of the local scope:
def my_func(n):
    global var
    var = 'hello world'
    return n ** 2

# print(var) # no var here because the function is not run

my_func(2)
print(var)


# Beware!!
# Remember that whenever you assign a value to a variable without having specified the variable as global, it is local in the current scope. Moreover, it does not matter where the assignment in the code takes place, the variable is considered local in the entire scope - Python determines the scope of objects at compile-time, not at run-time.

# Let's see an example of this:
a = 10
b = 100

def my_func():
    print(a)
    print(b)

my_func()

# BUT: 

def my_func():
    print(a)
    print(b)
    b = 1000

# my_func() # it will cause error


# Of course, functions are also objects, and scoping applies equally to function objects too. For example, we can "mask" the built-in print Python function:

print = lambda x: 'hello {0}'.format(x)

def my_func(name):
    return print(name)

print(my_func('world'))

del print

print("Hello, world")

for i in range(10):
    x = 2 * i

print(x)
