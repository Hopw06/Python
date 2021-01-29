## simplify algorithm ##

def f(a, b, c):
    l = 0
    for x in a:
        l += x
    for x in b:
        l += 2*x
    for x in c:
        l += 3*x
    return l

print(f(range(0,10), range(0,10), range(0,10)))

# we can simplify it by using nested function
def f(a, b, c):

    def inner(l, c):
        s = 0
        for x in l:
            s += x * c
        return s
    
    l = 0
    l += inner(a, 1)
    l += inner(b, 2)
    l += inner(c, 3)
    return l    

print(f(range(0,10), range(0,10), range(0,10)))

# or even better by using lambda

def f(a, b, c):
    l = 0
    inner = lambda l, c: sum([x* c for x in l])
    l += inner(a, 1)
    l += inner(b, 2)
    l += inner(c, 3)
    return l

print(f(range(0,10), range(0,10), range(0,10)))

## Pass as argument: it is used when we want something generic. 
# an example on sorting elements.
employees = [
    {'first_name': 'John', 'last_name': 'Joseph'},
    {'first_name': 'Celine', 'last_name': 'Adams'},
    {'first_name':'Paul', 'last_name': 'Johnson'},
    {'first_name': 'Aswathy', 'last_name': 'Govind'}
]

def order(names):
    def inner(item):
        return item['first_name']
    sl = zip(range(1,10), sorted(names, key=inner))
    return list(sl)

print(order(employees))

# try to sort with last_name

def order(names):
    def inner(item):
        return item['last_name']
    sl = zip(range(1,10), sorted(names, key=inner))
    return list(sl)

print(order(employees))

# by pass a function as a key of sorted function, we can change the rule on sorting elements easily. 

## dynamic function ## 
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

print(square(2))

print(cube(3))

# by using dynamic function:
def fpower(exp):
    inner = lambda x: x ** exp
    return inner

square = fpower(2)
print(square(2))

cube = fpower(3)
print(cube(3))

# we can create many function with dynamic function
quartic = fpower(4)
quintic = fpower(5)

print(quartic(4))
print(quintic(5))

## Encapsulation ##
# The nested function inside a function is only callable inside this function.

def outer(num1):
    def inner(num1):
        return num1 + 1
    num2 = inner(num1)
    print(num1, num2) 

outer(1)

# inner(1) error

def factorial(number):
    if not isinstance(number, int):
        raise TypeError("Sorry, number must be an integer")
    if number < 0:
        raise ValueError("Sorry, number must be zero or positive")

    def inner(number):
        if number < 1:
            return 1
        return number * inner(number - 1)
    return inner(number)

factorial(10)

# factorial(-1)

# By using this feature, we can check some conditions before actually call recursive.

## DRY - Don't repeat yourself ##

def process(file):
    def do_something(processing_file):
        for line in processing_file:
            print(line)
    
    if isinstance(file, str):
        with open(file, 'r') as f:
            do_something(f)
    else:
        do_something(file)

## Closures ## the best way to use nested function3
# It mean functions which can remember the environment where they were created.

def make_printer(msg):
    def printer():
        print(msg)
    return printer

printer = make_printer('Foo!')
printer()

# A closure is include two conditions:
# 1. access to variables in the scope where the closure was created.
# 2. access to these variables when it is called.

# an example: not closure: #

def make_printer(msg):
    def printer(msg=msg): # use msg as default value.
        print(msg)
    return printer

printer = make_printer('Foo!')
printer()

# An example in in dynamic function section.