## *arg ##
# we can use a similar concept in function definitions to allow for arbitrary numbers of positional parameters/arguments:

def func1(a, b, *arg):
    print(a)
    print(b)
    print(type(arg))
    print(arg)

func1(1, 2, 'a', 'b', 'c')

# A few things to note:
# 1. Unlike iterable unpacking, *arg will be a tuple, not a list.
# 2. The name of the parameter args can be anything you prefer.
# 3. You cannot specify positional arguments after the *arg parameter.

def avg(*args):
    count = len(args)
    total = sum(args)
    if count == 0:
        return 0
    else:
        return total/count

print(avg(1, 2, 3, 4, 5))

# print(avg()) # error

# make sure have at least one element

def avg_1(a, *args):
    count = len(args) + 1
    total = sum(args) + a
    return total/count

print(avg_1(1, 2, 3, 4, 5))

## Unpacking an iterable into positional arguments ##
def func1(a, b, c):
    print(a)
    print(b)
    print(c)

l = [10, 20, 30]

# func1(l) error

func1(*l)
