# Here, we will cover some understanding of classes in Python and how to create them
# to create a custom class, we use the class keyword, and we can initialize class attributes in the special method __init__

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(the_referenced_object):
        return 2 * (the_referenced_object.height + the_referenced_object.width)
    
    def __str__(self):
        return 'Rectangle (width={0}, height={1})'.format(self.width, self.height)
    
    def __repr__(self):
        return 'Rectangle ({0}, {1})'.format(self.width, self.height)
    
    def __eq__(self, other):
        print('self = {0}, other = {1}'.format(self, other))
        if isinstance(other, Rectangle):
            return (self.width, self.height) == (other.width, other.height)
        else:
            return False
    
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


# we create an instance of Rectangle, by pass arguments as the second and third arguments of __init__ method
r1 = Rectangle(10, 20)

# The first arguiment self contains the object being created.

print(r1.width)

print(r1.height)

# self is just convention, we can use other name to refer to object.
# such as perimeter method
print(r1.area())
print(r1.perimeter())

# Python defines a bunch of special methods
# These special methods provide us an easy way to overload operators in Python.
# example __str__() function

print(str(r1))

# other method __repr__ 
r1

# There are methods such as __lt__, __gt__, __le__, __eq__ used to compare

r2 = Rectangle(15, 20)

print(r1 == r2)


print(r1 < r2)

print(r2 < r1)

# What about > 

print(r1 > r2) # Since < is defined, so it will give "r1 < r2" a try.

# In Java, we often write getter/setter for properties. But it is nessesary only when we have some logic in getter/setter for
# Such as check value before assign to property. 
# Problem: At first time, maybe we don't have any logic to check with, so we can access properties directly. 
# But then, when we need to make getter/setter, it will break the code that access properties directly. 
# => That's why we always write getter/setter from begining.

# But is's not problem in Python. Here is an example.

class Square:
    def __init__(self, edge):
        self._edge = None
        self.edge = edge
    
    def __repr__(self):
        return 'Square ({0})'.format(self.edge)
    
    @property
    def edge(self):
        return self._edge
    
    @edge.setter
    def edge(self, edge):
        if edge <= 0:
            raise ValueError("Edge must be positive!!!")
        self._edge = edge

s = Square(10)

print(s)

s.edge = 20

print(s)

s.edge = -10 # Error

print(s)

s1 = Square(-10) # Error

print(s1)

# Above in Square class, we check edge positive in setter and __init__