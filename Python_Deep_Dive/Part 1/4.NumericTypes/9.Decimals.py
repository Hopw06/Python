import decimal
from decimal import Decimal

# Decimal have context, that can be used to specify rounding and precision (amongst other things)

# Context can be local (temporary contexts) or global (default)

## Global Context ##
g_ctx = decimal.getcontext()

print(g_ctx.prec, g_ctx.rounding)

g_ctx.prec = 6
g_ctx.rounding = decimal.ROUND_HALF_UP

print(g_ctx.prec, g_ctx.rounding)

## Local Context ##
# The localcontext() function will return a context manager that we can use with a with statement:
with decimal.localcontext() as ctx: # make a copy of global context
    print(ctx.prec)
    print(ctx.rounding)

    # we can change it
    ctx.prec = 12
    ctx.rounding = decimal.ROUND_HALF_EVEN

    print(ctx.prec, ctx.rounding)

## Rounding ##
g_ctx.rounding = decimal.ROUND_HALF_EVEN
print(g_ctx.prec, g_ctx.rounding)
x = Decimal('1.25')
y = Decimal('1.35')

print(round(x, 1), round(y, 1))
with decimal.localcontext() as ctx:
    ctx.rounding = decimal.ROUND_HALF_UP
    print(round(x, 1), round(y, 1))

print(round(x, 1), round(y, 1))

# Local context do not effect the global context