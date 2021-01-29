print(True or True and False) # because of and having higher precendence than or

print(True or (True and False))

print((True and True) and False)

a = 10
b = 2

if a / b > 2:
    print('a is at least double b')

b = 0
# if a / b > 2: # error
#     print('a is at least double b')

if b and a / b > 2:
    print('a is at least double b')

# name = ''
# if name[0] in string.digits: # error
#     print('Name can not start with a digit!')
import string
name = ''
if name and name[0] in string.digits:
    print('Name can not start with a digit!')

name = None
if name and name[0] in string.digits:
    print('Name can not start with a digit!')

name = '1Bob'
if name and name[0] in string.digits:
    print('Name can not start with a digit!')