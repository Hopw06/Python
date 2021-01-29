def my_func(a, b, c):
    print("a={0}, b={1}, c={2}".format(a, b, c))

my_func(1, 2, 3)

## Default values ##
def my_func1(a, b = 3, c = 3):
    print("a={0}, b={1}, c={2}".format(a, b, c))

my_func1(1)

my_func1(1, 2)

my_func1(1, 2, 3)

# Note that if once a parameter is assigned a default value, all parameters thereafter must be assigned a default value too!
def fn(a, b=2, c): # error
    print(a, b, c)

# my_func1() # error, c is not assigned to any defalt value. 

## Keyword Arguments ##
my_func1(c = 20, a = 10, b = 5)

my_func1(10, c = 3, b = 2)

# Note that if once a keyword argument has been used, all arguments thereafter must also be named:
# my_func1(10, b=20, 30) # error.

# But if a parameter has a default value, it can be ommitted from the argument list
my_func1(10, c=30)
my_func1(a=10, c=30)
my_func1(c=30, a=10)