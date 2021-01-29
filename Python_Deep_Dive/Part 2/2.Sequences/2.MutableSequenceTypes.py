## Replace elements ##
l = [1, 2, 3, 4, 5]
print(id(l))
l[0] = 'a'
print(id(l), l)

# We can also replace elements using slicing and extended slicing.
l = [1, 2, 3, 4, 5]
print(id(l))
l[0:2] = ['a', 'b', 'c', 'd', 'e']
print(id(l), l)

## Appending and Extending ##
l = [1, 2, 3]
print(id(l))
l.append(4)
print(id(l), l)

l = [1, 2, 3]
print(id(l))
l = l + [4]
print(id(l), l)

l = [1, 2, 3, 4, 5]
print(id(l))
l.extend({'a', 'b', 'c'})
print(id(l), l)

l = [1, 2, 3]
l.extend(('a', 'b', 'c'))
print(l)

## Removing elements ##
# using pop function
l = [1, 2, 3, 4]
print(id(l))
popped = l.pop(1)
print(id(l), popped, l)

l = [1, 2, 3, 4]
popped = l.pop()
print(popped)
print(id(l), popped, l)

#using clear function
l = [1, 2, 3, 4]
print(id(l))
l.clear()
print(id(l), l)

# different with re assign
l = [1, 2, 3, 4]
print(id(l))
l = []
print(id(l), l)

## Inserting elements ##
l = [1, 2, 3, 4]
print(id(l))
l.insert(1, 'a')
print(id(l), l)

## Reversing a sequence ##
# in place:
l = [1, 2, 3, 4]
print(id(l))
l.reverse()
print(id(l), l)
# change id:
l = [1, 2, 3, 4]
print(id(l))
l = l[::-1]
print(id(l), l)

## Copying sequences ##
l = [1, 2, 3, 4]
print(id(l))
l2 = l.copy()
print(id(l2), l2)

# equal with:

l = [1, 2, 3, 4]
print(id(l))
l2 = l[:]
print(id(l2), l2)