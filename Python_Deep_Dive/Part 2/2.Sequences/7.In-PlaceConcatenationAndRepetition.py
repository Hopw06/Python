## In-Place Concatenation ##
l1 = [1, 2, 3, 4]
l2 = [5, 6]

print(id(l1), l1)
print(id(l2), l2)

l1 = l1 + l2
print(id(l1), l1) # new object

l1 = [1, 2, 3, 4]
l2 = [5, 6]

print(id(l1), l1)
print(id(l2), l2)

l1 += l2
print(id(l1), l1) # same object

# It work with other iterables as well:

l1 = [1, 2, 3, 4]
t1 = 5, 6, 7
print(id(l1), l1)
print(id(t1), t1)

l1 += t1
print(id(l1), l1)

l1 += range(8, 11)
print(id(l1), l1)

# or even with iterable non-sequence types:
l1 += {11, 12, 13}
print(id(l1), l1)

# of course, it will not work with immutable object.
t1 = 1, 2, 3
t2 = 4, 5, 6
print(id(t1), t1)
print(id(t2), t2)

t1 += t2
print(id(t1), t1) # new object

## In-Place Repetition ##
l = [1, 2, 3]
print(id(l), l)

l *= 2
print(id(l), l)

t = (1, 2, 3)
print(id(t), t)

t *= 2
print(id(t), t)