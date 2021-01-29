## The Decimal constructor can handle a variety of data types. ## 
import decimal
from decimal import Decimal

print(Decimal(10))

print(Decimal('10'))

print(Decimal(-10))

print(Decimal('-10'))

# But do not use float in decimal constructor
print(format(0.1, '.25f'))

print(Decimal(0.1))

# As you can see, decimal try to represent that binary float exactly. 
# So, instead, just pass a string to it.

print(Decimal('0.1'))

## Context Precision and the Constructor ##
decimal.getcontext().prec = 2

a = Decimal('0.12345')
b = Decimal('0.12345')

print(a)
print(b)
print(a + b)
# precision doesn't effect when creating a Decimal object, but when perform operator, it will round up. 

## Local and Global Contexts are independent ##
decimal.getcontext().prec = 6
print(decimal.getcontext().rounding)

a = Decimal('0.12345')
b = Decimal('0.12345')
print(a + b)
with decimal.localcontext() as ctx:
    ctx.prec = 2
    c = a + b
    print('c within local context: {0}'.format(c))
print('c within global context: {0}'.format(c)) # since c was created in local context.