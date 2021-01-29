t = 10, 3, 5, 8, 9, 6, 1
print(sorted(t))

s = {10, 3, 5, 8, 9, 6, 1}
print(sorted(s))

d = {3: 100, 2: 200, 1: 10}
for item in d:
    print(item)

print(sorted(d))

d = {'a': 100, 'b': 50, 'c':10}
print(sorted(d, key=lambda k: d[k]))

t = 'this', 'parrot', 'is', 'a', 'late', 'bird'
print(sorted(t))

print(sorted(t, key=lambda s: len(s)))

import this

c = 0, 10 + 10j, 3 - 3j, 4 + 4j, 5 - 2j
print(sorted(c, key = abs))
print(sorted(c, key = lambda x: x.imag))

## Reversed Sort ##

print(sorted(t, key=lambda s: len(s)))
print(sorted(t, key=lambda s: len(s), reverse=True))
# or
print(sorted(t, key=lambda s: -len(s)))

## In Place Sorting ##
l = list(t)
print(id(l))
print(l.sort(key=lambda s: len(s)))

print(l, id(l))