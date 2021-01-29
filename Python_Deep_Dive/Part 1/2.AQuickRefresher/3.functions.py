# Python has many built-in functions and methods we can use. 
# Some are available by default:

s = [1, 2, 3]
print(len(s))

# While some need to be imported
from math import sqrt
print(sqrt(4))

# Entire modules can be imported
import math
print(math.exp(1))

# We can define our own functions:
def func_1():
    print("running func1")

func_1()

# Note that to "call" or "invoke" a function we need to use the ().
# Simple using the function name without the () refers to the function, but does not call it:
print(func_1)

# We can also define functions that take parameters:
def func_2(a, b):
    return a * b
# Note that a and b can be any type.
# But the function will fail to run if a and b are types that are not "compatible" with the * operator:

print(func_2(3, 2))
print(func_2('a', 3))
print(func_2([1, 2, 3], 2))

func_2('a', 'b') # => error
# It is possible to use type annotations:
def func_3(a: int, b: int):
    return a * b

print(func_3(2, 3)) # 6
print(func_3('a', 2)) # 'aa'

# But as you can see, these do not enforce a data type! They are simple metadata that can be used by external libraries, and many IDE's.
# Functions are objects, just like integers are objects, and they can be assigned to variables just as an integer can:

my_func = func_3
print(my_func('a', 2))

# Functions must always return something. If you do not specify a return value, Python will automatically return the None object:
def func_4():
    # does something but does not return a value
    a = 2

res = func_4()
print(res)

# The def keyword is an executable piece of code that creates the function (an instance of the function class) and essentially assigns it to 
# a variable name (the function name).

# note that the function is defined when def is called, but the code inside it is not evaluated until the function is called.
# This why we can call other functions inside a function which will be defined later - as long as we do not call them before all necessary function are defined.  

# for example, the following will work:
def fn_1():
    fn_2()

def fn_2():
    print("Hello")

fn_1()
# but this will not work:

def fn_3():
    fn_4()

fn_3()

def fn_4():
    print("Hello")

lambda, used to create a new function and assign it to a variable.

func_5 = lambda x: x**2

print(func_5)
print(func_5(2))
