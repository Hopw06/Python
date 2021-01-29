# Split a list into it's first element, and "everything else" using slicing:
l = [1, 2, 3, 4, 5, 6]

a = l[0]
b = l[1:]
print(a, b)

# using unpacking:
a, b = l[0], l[1:]
print(a, b)

#or using * operator:
a, *b = l
print(a, b)

# Note that * operator can only appear once!

# Like standard unpacking, extended unpacking will work with any iterable:
# tupple
a, *b = -10, 5, 2, 100
print(a, b)

# string
a, *b = "python"
print(a, b)

# first, second, last element and the rest:
s = "python"
a, b, c, d = s[0], s[1], s[2:-1], s[-1]
print(a, b, c, d, sep="\n")

# Or we can simply use unpacking:
a, b, *c, d = s
print(a, b, ''.join(c), d, sep="\n")

# We can also use unpacking on the right hand side of an assignment expression:
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [*l1, *l2]
print(l)

l1 = [1, 2, 3]
s = 'ABC'
l = [*s, *l1]
print(l)

# This unpacking works with unordered types such as sets and dictionaries as well.
# The only thing is that it may not be very useful considering, there is no particular ordering, so a first or last element has not real useful meaning.

s = {10, -99, 3, 'd'}
for c in s:
    print(c)

# As you can see, the order of the elements when we created the set was not retained.

# In this case, unpacking is useful when we need to combine things together. 
s1 = {1, 2, 3}
s2 = {4, 5, 6}

#s1 + s2, no such operator
# we can use union function
print(s1.union(s2))

# But what about more set:
s3 = {7, 8, 9}
s4 = {10, 11, 12}

print(s1.union(s2, s3, s4))

# Or simply
s5= {*s1, *s2, *s3, *s4}
print(s5)

# The same works for dictionaries:
d1 = {'key1':'value1', 'key2':'value2'}
d2 = {'key2':'value3', 'key3':'value4'}

d = {*d1, *d2}
print(d) # it only get the keys

# we can use ** operator

d = {**d1, **d2}
print(d) # key2 value will be override

d = {**d2, **d1}
print(d) # key2 value will be override

# we can use unpacking inside dictionaries:
d = {'a': 1, 'b': 2, **d1, **d2, 'c': 3}
print(d)

# Again, if the key is same, only the latest value of the key is retained:
d = {'key1': 100, **d1, **d2, 'key3': 200}
print(d)

## NESTED UNPACKING ##
a, b, (c, d) = [1, 2, 'XY']
print(a)
print(b)
print(c)
print(d)

a, b, (c, d, *e) = [1, 2, 'python']
print(a)
print(b)
print(c)
print(d)
print(e)