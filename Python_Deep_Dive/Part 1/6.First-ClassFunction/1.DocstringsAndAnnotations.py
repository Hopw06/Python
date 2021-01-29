## Docstrings ##
# help function used to display information about function
help(print)

def my_function(a, b):
    return a + b

help(my_function)

# let's add some information:

def my_function(a, b):
    'return sum of two number (a and b)'
    return a + b

help(my_function)

# Docstrings can span multiple lines using a multi-line string literal:
def fact(n):
    '''Calculates n! (factorial function)
    
    Inputs:
        n: non-negative integer
    Returns:
        the factorial of n
    '''

    if n < 0:
        '''Note that this is not part of the docstrings!'''
        return 1
    else:
        return n * fact(n - 1)

help(fact)

# we can display docstrings this way:
print(fact.__doc__)

## Annotations ##


def my_func(a:'annotation for a', b:'annotation for b')->'annotation for return':
    return a + b

my_func(2, 3)

help(my_func)


# Note that these annotations do not force a type on the parameters or the return value - they are simply there for documentation purposes within Python and may be used by external applications and modules, such as IDE's.

print(my_func.__annotations__)


# Of course we can combine both docstrings and annotations:

def fact(n: 'int >= 0')->int:
    '''Calculates n! (factorial function)
    
    Inputs:
        n: non-negative integer
    Returns:
        the factorial of n
    '''
    
    if n < 0:
        '''Note that this is not part of the docstring!'''
        return 1
    else:
        return n * fact(n-1)

help(fact)

# Annotations will work with default parameters too: just specify the default after the annotation:

def my_func(a:str='a', b:int=1)->str:
    return a*b

my_func()
help(my_func)