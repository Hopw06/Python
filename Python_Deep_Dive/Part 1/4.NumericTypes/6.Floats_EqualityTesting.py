# Because not all real numbers have an exact float representaion:
x = 0.1 + 0.1 + 0.1
y = 0.3
print(x == y)

# This is because 0.1 and 0.3 do not have exact representations:

print('0.1 --> {0:.25f}'.format(0.1))
print('x --> {0:.25f}'.format(x))
print('y --> {0:.25f}'.format(y))

# However:
x = 0.125 + 0.125 + 0.125 
y = 0.375
print(x == y)

print('0.125 --> {0:.25f}'.format(0.125))
print('x --> {0:.25f}'.format(x))
print('y --> {0:.25f}'.format(y))

# One way to solve the problem
x = 0.1 + 0.1 + 0.1
y = 0.3
print(round(x, 5) == round(y, 5))

# Or use iscolse function:
from math import isclose
x = 0.1 + 0.1 + 0.1
y = 0.3
print(isclose(x, y))

'''
The isclose method takes two optional parameters, rel_tol and abs_tol.

rel_tol is a relative tolerance that will be relative to the magnitude of the largest of the two numbers being compared. Useful when we want to see if two numbers are close to each other as a percentage of their magnitude.

abs_tol is an obsolute tolerance that is independent of the magnitude of the number being compared. This is useful for numbers that are close to zero.
'''

print(isclose(123456789.01, 123456789.01, rel_tol=0.01))

print(isclose(0.01, 0.02, rel_tol=0.01))

x = 0.0000000001
y = 0.0000000002

print(isclose(x, y, rel_tol=0.01)) # false

print(isclose(x, y, rel_tol= 0, abs_tol= 0.0001))

# In general, we can combine the use of both relative and absolute tolerances in this way:

x = 0.0000000001
y = 0.0000000002

a = 123456789.01
b = 123456789.02

print('x = y: ', isclose(x, y, abs_tol=0.0001, rel_tol=0.01))
print('a = b: ', isclose(a, b, abs_tol=0.0001, rel_tol=0.01))