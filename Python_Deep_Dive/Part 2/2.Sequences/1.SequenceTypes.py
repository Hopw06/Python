# Sequence Types
## Iterables ##
t = (10, 'a', 1 + 3j)
s = {10, 'a', 1 + 3j}

for c in t:
    print(c)

for c in s:
    print(c)

print('a' in ['a', 'b', 100])
print(100 in range(200))

## Min, Max and Length ##

print(len('python'), len([1, 2, 3]), len({10, 20, 30}), len({'a': 1, 'b': 2}))

a = [100, 300, 200]
print(min(a), max(a))

s = 'python'
print(min(s), max(s))

s = {'p', 'y', 't', 'h', 'o', 'n'}
print(min(s), max(s))

a = [1 + 1j, 2 + 2j, 3 + 3j]
# print(min(a), max(a)) # not support. Do not have (< or >) operator

from decimal import Decimal

t = 10, 20.5, Decimal('30.5')
print(min(t), max(t))

t = ['a', 10, 1000]
# print(min(t)) # '<' not supported between instances of 'int' and 'str'

r = range(10, 200)
print(min(r), max(r))

## Concatenation ##
print([1, 2, 3] + [4, 5, 6])
print((1, 2, 3) + (4, 5, 6))

# print((1, 2, 3) + [4, 5, 6]) # error
# print('abc' + ['d', 'e', 'f']) # error

print((1, 2, 3) + tuple([4, 5, 6]))
print(tuple('abc') + ('d', 'e', 'f'))
print(''.join(tuple('abc') + ('d', 'e', 'f')))

## Repetition ##
print('abc' * 5)
print([1, 2, 3] * 5)

## Finding things in Sequences ##
s = "gnu's not unix"

print(s.index('n'))

print(s.index('n', 1), s.index('n', 2), s.index('n', 8))

# print(s.index('n', 13))

try:
    idx = s.index('n', 13)
except ValueError:
    print('not found')

## Slicing ##
s = 'python'
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(s[0:3], s[4:6])
print(l[0:3], l[4:6])

print(s[4:1000])

print(s[0:3], s[:3])

print(s[0:3], s[:3])
print(s[3:1000], s[3:], s[:])

print(s, s[0:5], s[0:5:2])
print(s, s[::2], s[::-1], s[::-2])

r = range(11)

print(r)
print(list(r))

print(r[:5])
print(list(r[:5]))

## Hashing ##

l = (1, 2, 3)
print(hash(l))

s = '123'
print(hash(s))

r = range(10)
print(hash(r))

l = [1, 2, 3]
# print(hash(l)) # can not hash

t = (1, 2, [10, 20])
# print(hash(t)) # can not hash

from decimal import Decimal
d = Decimal(10.5)
print(hash(d))

s = {1, 2, 3}
# print(hash(s))

s = frozenset({1, 2, 3}) # immutable set
print(hash(s))

## Caveats with Concatenation and Repetition ##
x = [2000]

print(id(x[0]))

l = x + x
print(l)
print(id(l[0]), id(l[1]))
print(l[0] is l[1])

# This is not a big deal if the objects being concatenated are immutable. But if they are mutable:

x = [[0, 0]]
l = x + x

print(l)
print(l[0] is l[1])

l[0][0] = 1000

print(l)
print(x)

x = [[0, 0]]
m = x * 3

print(m)
m[0][0] = 100
print(m)
print(x)


# If you really want these repeated objects to be different objects, you'll have to copy them somehow. A simple list comprehensions would work well here:
x = [[0, 0] ]
m = [e.copy() for e in x*3]

print(m)
m[0][0] = 1000

print(m)
print(x)