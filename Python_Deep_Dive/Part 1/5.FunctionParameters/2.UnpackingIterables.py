## note on tuples ##
a = (1, 2, 3)
print(type(a))

a = 1, 2, 3
print(type(a))

#in fact what defines a tuple is not (), but the , (comma)
a = (1)
print(type(a))


a = (1, )
print(type(a))

a = 1,
print(type(a))
# or we can use tuple constructor:
a = tuple()
print(type(a))

## Unpacking ##
l = [1, 2, 3, 4]
a, b, c, d = l
print(a, b, c, d)

a, b, c = 'XYZ'
print(a, b, c)

## Unpacking Unordered Objects ##
dict1 = {'p': 1, 'y': 2, 't': 3, 'h': 4, 'o': 5, 'n': 6}
print(dict1)

for c in dict1:
    print(c)

a, b, c, d, e, f = dict1
print(a, b, c, d, e, f)

# The same applies to sets
s = {'p', 'y', 't', 'h', 'o', 'n'}
print(type(s))
print(s)

for c in s:
    print(c)

a, b, c, d, e, f = s
print(a, b, c, d, e, f)