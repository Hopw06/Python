squares = []
for i in range(1, 101):
    squares.append(i**2)
print(squares[0:10])

squares = [i**2 for i in range(1, 101)]
print(squares[0:10])

squares = []
for i in range(1, 101):
    if i % 2 == 0:
        squares.append(i**2)
print(squares[0:10])

squares = [i**2 for i in range(1, 101) if i % 2 == 0]
print(squares[0:10])

## Nested Comprehensions ##
table = []
for i in range(1, 11):
    row = []
    for j in range(1, 11):
        row.append(i*j)
    table.append(row)

print(table)

table2 = [ [i*j for j in range(1, 11)] for i in range(1, 11)]
print(table2)

from math import factorial

def combo(n, k):
    return factorial(n) // factorial(k) * factorial(n - k)

size = 10
pascal = [ [combo(n, k) for k in range(n + 1)] for n in range(size + 1)]
print('\n'.join([str(i) for i in pascal])) 

## Nested Loops ##
l1 = ['a', 'b', 'c']
l2 = ['x', 'y', 'z']
result = []
for s1 in l1:
    for s2 in l2:
        result.append(s1 + s2)

print(result)

rs = [s1 + s2 for s1 in l1 for s2 in l2]
print(rs)

l1 = ['a', 'b', 'c']
l2 = ['b', 'c', 'd']

result = []
for s1 in l1:
    for s2 in l2:
        if s1 != s2:
            result.append(s1 + s2)

rs = [s1 + s2 for s1 in l1 for s2 in l2 if s1 != s2]

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = ['a', 'b', 'c', 'd']

print(list(zip(l1, l2)))

result = []
for index_1, item_1 in enumerate(l1):
    for index_2, item_2 in enumerate(l2):
        if index_1 == index_2:
            result.append((item_1, item_2))

print(result)

result = [ (item_1, item_2)
        for index_1, item_1 in enumerate(l1)
        for index_2, item_2 in enumerate(l2)
        if index_1 == index_2]

print(result)

v1 = (1, 2, 3, 4, 5, 6)
v2 = (10, 20, 30, 40, 50, 60)

dot = 0
for i in range(len(v1)):
    dot += (v1[i] * v2[i])
print(dot)

dot = sum([i*j for i, j in zip(v1, v2)])
print(dot)

## Things to watch out for ##
if 'number' in globals():
    del number

l = [number**2 for number in range(5)]
print(l)

print('number' in globals())

number = 100
l = [number**2 for number in range(5)]
print(l)
print(number)

number = 100
l = [number*i for i in range(5)]
print(l)

if 'i' in globals():
    del i

funcs = []
for i in range(6):
    funcs.append(lambda x: x**j)

print(funcs[0](10))
print(funcs[1](10))
print(funcs[2](10))
print(funcs[3](10)) # all are same

# because it refer to the same i variable as i is in globals
print(i)

funcs = [lambda x: x**i for i in range(6)]

print(funcs[0](10))
print(funcs[1](10))
print(funcs[2](10))
print(funcs[3](10)) # all are same

# because it refer to the same i variable in local Comprehensions
funcs = [lambda x, pow=i: x**pow for i in range(6)]

print(funcs[0](10))
print(funcs[1](10))
print(funcs[2](10))
print(funcs[3](10))
# make a default value when define a new function