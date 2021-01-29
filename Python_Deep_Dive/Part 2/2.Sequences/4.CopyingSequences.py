## Shallow Coppies ##
# 1. simple loop

l1 = [1, 2, 3]
l1_copy = []

for item in l1:
    l1_copy.append(item)

print(l1 is l1_copy)

# 2. List Comprehension
l1 = [1, 2, 3]
l1_copy = [item for item in l1]
print(l1_copy)

print(l1 is l1_copy)

# 3. Using the copy() method
l1 = [1, 2, 3]
l1_copy = l1.copy()
print(l1_copy)

print(l1 is l1_copy)

# 4. Using the built-in list() function
l1 = [1, 2, 3]

l1_copy = list(l1)
print(l1_copy)

print(l1 is l1_copy)

# we can copy any iterator into a list
l1_copy = list((1, 2, 3))
print(l1_copy)

# But watch out for tuple() function
t1 = (1, 2, 3)
t1_copy = tuple(t1)
print(t1_copy)
print(t1 is t1_copy)

# 5. Using slicing

l1 = [1, 2, 3]
l1_copy = l1[:]
print(l1_copy)
print(l1 is l1_copy)

# But again, watch out with immutable objects
t1 = (1, 2, 3)
t1_copy = t1[:]
print(t1_copy)
print(t1 is t1_copy)

s1 = "Python"
s2 = str(s1)
print(s2)
print(s1 is s2)

s1 = "Python"
s2 = s1[:]
print(s2)
print(s1 is s2)

# 6. Using the copy module
import copy

l1 = [1, 2, 3]
l1_copy = copy.copy(l1)
print(l1_copy)
print(l1 is l1_copy)

# tuples:
t1 = (1, 2, 3)
t1_copy = copy.copy(t1)
print(t1_copy)
print(t1 is t1_copy)

## Shallow vs Deep Coppies ##
# Shallow means that when a sequence is copied, each element of the new sequence is bound to precisely the same memory address as the corresponding element in the original sequence:

v1 = [0, 0]
v2 = [0, 0]

line1 = [v1, v2]
print(line1)
print(id(line1[0]), id(line1[1]))

line2 = line1.copy()

print(line1 is line2)
print(id(line1[0]), id(line1[1]))
print(id(line2[0]), id(line2[1]))

line2[0][0] = 100

print(line2)
print(line1)

# So we can do as follows:
v1 = [0, 0]
v2 = [0, 0]

line1 = [v1, v2]
line2 = [item[:] for item in line1]
print(id(line1[0]), id(line1[1]))
print(id(line2[0]), id(line2[1]))

line1[0][0] = 100
print(line1)
print(line2)

# problem is when we have multiple level in element
# the deepcopy() function

v1 = [0, 0]
v2 = [0, 0]
line1 = [v1, v2]
line2 = copy.deepcopy(line1)
print(id(line1[0]), id(line1[1]))
print(id(line2[0]), id(line2[1]))

line2[0][0] = 100
print(line1)
print(line2)

# it works with any level of nested objects
v1 = [11, 12]
v2 = [21, 22]
line1 = [v1, v2]

v3 = [31, 32]
v4 = [33, 34]
line2 = [v3, v4]

plane1 = [line1, line2]
print(plane1)

plane2 = copy.deepcopy(plane1)
print(plane2)

print(plane1[0], id(plane1[0]))
print(plane2[0], id(plane2[0]))

print(plane1[0][0], id(plane1[0][0]))
print(plane2[0][0], id(plane2[0][0]))

## Even works with custom classes ##
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Point({self.x}, {self.y})'

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return f'Line({self.p1.__repr__()}, {self.p2.__repr__()})'

p1 = Point(0, 0)
p2 = Point(10, 10)
line1 = Line(p1, p2)
line2 = copy.deepcopy(line1)

print(line1.p1, id(line1.p1))
print(line2.p1, id(line2.p1))

# If we use a shallow copy
p1 = Point(0, 0)
p2 = Point(10, 10)
line1 = Line(p1, p2)
line2 = copy.copy(line1)

print(line1.p1, id(line1.p1))
print(line2.p1, id(line2.p1))