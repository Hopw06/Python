# to solve the issue: No positional arguments after the *arg parameter.
# we can use keyword arguments
def func(a, b, *args, d):
    print(a, b, args, d)

# func(10, 20, 'a', 'b', 100) # error

# but this will work: 
func(10, 20, 'a', 'b', d=100)

def func1(*args, d):
    print(args)
    print(d)

func1(1, 2, 3, d='hello')

func1(d='hello')

# func1()# error

# Use default values
def func1(*args, d='n/a'):
    print(args)
    print(d)

func1(1, 2, 3)

func1()

# Sometimes we want only keyword arguments, in which case we still have to exhaust the positional arguments first - but we can use the following syntax if we do not want any positional parameters passed in:
def func1(*, d='hello'):
    print(d)

# func1(10, d='bye')

func1(d='bye')

def func1(*, a, b):
    print(a, b)

func1(a=10, b=10) # only keyword arguments

# func1(10, 20) # error