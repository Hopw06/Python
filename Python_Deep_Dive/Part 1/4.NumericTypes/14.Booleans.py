# bool class is used to represent boolean values.
# the bool class inherits from the int class.
print(issubclass(bool, int))

print(type(True), id(True), int(True))

print(type(False), id(False), int(False))

print(isinstance(True, bool))
print(isinstance(False, bool))

print(isinstance(True, int)) # 1
print(isinstance(False, int)) # 0

# since True and False are singleton, we can use is or == operator to compare them to any boolean expression.
print(id(True), id(1 < 2))
print(id(False), id(1 == 3))

print((1 < 2) is True, (1 < 2) == True)
print((1 == 2) is False, (1 == 2) == False)

# cast value to boolean
print(bool(1), bool(100), bool(-100)) # value != 0 equal to True
print(bool(0))

# Because it is subclass of int. It can perform operators like int. 
print(True > False)

print(True * 3) # 1 * 3

print(True / 3) # 1 / 3

import math
print(math.sqrt(True)) 