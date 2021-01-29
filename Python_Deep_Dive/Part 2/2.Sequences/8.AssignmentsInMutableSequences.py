## Replacement ##
l = [1, 2, 3, 4, 5]
print(id(l))
print(l[0:3])

l[0:3] = ['a', 'b', 'c', 'd']
print(l, id(l))

l = [1, 2, 3, 4, 5]
l[0:3] = 'python'

print(id(l), l)

## Deleting ##
# Delete is really just a special case of replacement
l = [1, 2, 3, 4, 5]
print(id(l))

l[0:1] = []
print(l, id(l))

l = [1, 2, 3, 4, 5]
print(id(l))

l[0:2] = []
print(l, id(l))

## Inserting ##
l = [1, 2, 3, 4, 5]
print(id(l))

## Inserting ##
l = [1, 2, 3, 4, 5]
print(id(l))

l[1:1] = 'abc'
print(l, id(l))

## Extended Slices ##
l = [1, 2, 3, 4, 5]
print(l, id(l))

l[::2] = 'abc'
print(l, id(l))
# e length of the slice and the length of the iterable we are setting on the right hand side must have the same length