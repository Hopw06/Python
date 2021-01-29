## Build an averager function ##
class Averager:

    def __init__(self):
        self.numbers = []
    
    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count

a = Averager()

print(a.add(10))

print(a.add(20))

print(a.add(30))

# We can do this using a closure as follows:

def averager():
    numbers = []

    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count
    return add


a = averager()

print(a(10))
print(a(20))
print(a(30))

# better design #

def averager():
    total = 0
    count = 0

    def add(number):
        nonlocal total, count
        total += number
        count += 1
        return total / count
    
    return add

a = averager()

print(a(10))
print(a(20))
print(a(30))

## Generalizing this example ##


# We saw that we were essentially able to convert a class to an equivalent functionality using closures. This is actually true in a much more general sense - very often, classes that define a single method (other than initializers) can be implemented using a closure instead.

# Let's look at another example of this.

# Suppose we want something that can keep track of the running elapsed time in seconds.

from time import perf_counter

class Timer:
    
    def __init__(self):
        self.start = perf_counter()

    
    def __call__(self):
        return (perf_counter() - self.start)

    
a = Timer()
b = Timer()

print(a())
print(b())

# using closure

def timer():
    start = perf_counter()

    def elapsed():

        return (perf_counter() - start)
    
    return elapsed


x = timer()
y = timer()

print(a())
print(b())
print(x())
print(y())