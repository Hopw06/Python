# Definition: A function that takes a function as an argument, and/or returns a function as its return value

# For example, the sorted function is a higher-order function as we saw in an earlier video.

## map ##
# The map built-in function is a higher-order function that applies a function to an iterable type object:
# form: map(func, *iterables)
# help(map)

def fact(n):
    return 1 if n < 2 else n * fact(n - 1)

print(fact(3))

rs = map(fact, [1, 2, 3, 4, 5])

print(rs)
print(type(rs))

# The map function returns a map object, which is an iterable - we can either convert that to a list or enumerate it:
l = list(rs)
print(l)

# we can also use it this way:
l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]

print(list(map(lambda x, y: x + y, l1, l2)))

## Filter ##
# The filter function is a function that filters an iterable based on the truthyness of the elements, or the truthyness of the elements after applying a function to them. Like the map function, the filter function returns an iterable that we can view by generating a list from it, or simply enumerating in a for loop.

l = [0, 1, 2, 3, 4, 5, 6]
for e in filter(None, l): # The element 0 is omitted
    print(e)

def is_even(x):
    return x & 1 == 0

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(is_even, l)
print(list(result))

## Alternatives to map and filter using Comprehensions ##
# factorial example:
l = [1, 2, 3, 4, 5]
rs = [fact(i) for i in l]
print(rs)

# Two iterables example:
# Before we do this example we need to know about the zip function.

# The zip built-in function will take one or more iterables, and generate an iterable of tuples where each tuple contains one element from each iterable:
l1 = 1, 2, 3
l2 = 'a', 'b', 'c'
print(list(zip(l1, l2)))

l1 = 1, 2, 3
l2 = 'abc'
l3 = [10, 20, 30]

print(list(zip(l1, l2, l3)))

#Using zip function, now we can add up two iterables
l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]

rs = [x + y for x, y in zip(l1, l2)]
print(rs)

# Filter using a Comprehensions
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rs = [i for i in l if i & 1 == 0]
print(rs)

## Combine map and filter ##
rs = list(filter(lambda y: y < 25, map(lambda x: x**2, range(10))))
print(rs)

# or using comprehensions
rs = [x**2 for x in range(10) if x**2 < 25]
print(rs)