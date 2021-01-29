def fact(n: "some non-negative integer") -> "n! or 0 if n < 0":
    """
    Calculates the factorial of a non-negative integer n.

    If n is negative, returns 0. 
    """
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    return n * fact(n - 1)

# Since functions are objects, we can add attributes to a function:
fact.short_description = "factorial function"

print(fact.short_description)

# We can see all the attributes that belong to a function using the dir function:
dir(fact)

#We can see our short_description attribute, as well as some attributes we have seen before: annotations and doc:
print(fact.__doc__)

print(fact.__annotations__)

def my_func(a, b=2, c=3, *, kw1, kw2=2, **kwargs):
    pass

f = my_func

print(f.__name__)

print(my_func.__name__)

print(f.__defaults__) # default values of any positional parameter.

print(f.__kwdefaults__) # default values of any keyword parameter

# Let's create a function with some local variables:

def my_func(a, b=1, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b

f = my_func

print(f.__code__) ## code object has attributes too (dir(f.__code__))
print(type(f.__code__))
print(f.__code__.co_varnames)
print(f.__code__.co_argcount)

## The inspect module ##
import inspect
print(inspect.isfunction(my_func))
print(inspect.ismethod(my_func)) # A method is a function that is bound to some object.

class MyClass:
    def f_instance(self):
        pass

    @classmethod
    def f_class(cls):
        pass

    @staticmethod
    def f_static():
        pass

# Instance methods are bound to the instance of a class (not the class itself)

# Class methods are bound to the class, not instances

# Static methods are no bound either to the class or its instances

print(inspect.isfunction(MyClass.f_instance), inspect.ismethod(MyClass.f_instance))

print(inspect.isfunction(MyClass.f_class), inspect.ismethod(MyClass.f_class))

print(inspect.isfunction(MyClass.f_static), inspect.ismethod(MyClass.f_static))

my_obj = MyClass()

print(inspect.isfunction(my_obj.f_instance), inspect.ismethod(my_obj.f_instance))

print(inspect.isfunction(my_obj.f_class), inspect.ismethod(my_obj.f_class))

print(inspect.isfunction(my_obj.f_static), inspect.ismethod(my_obj.f_static))

# If you just want to know if something is a function or method:

print(inspect.isroutine(my_obj.f_instance))

print(inspect.isroutine(my_obj.f_class))

print(inspect.isroutine(my_obj.f_static))

## Introspecting Callable Code ##
print(inspect.getsource(fact))

print(inspect.getmodule(fact))

import math

print(inspect.getmodule(math.sin))

# setting up variable
i = 10

# comment line 1
# comment line 2
def my_func(a, b=1):
    # comment inside my_func
    pass

print(inspect.getcomments(my_func))

## Introspecting Callable Signatures ##

# TODO: Provide implementation
def my_func(a: 'a string',
            b: int = 1,
            *args: 'additional positional arguments',
            kw1: 'first keyword-only arg',
            kw2: 'second keyword-only arg',
            **kwargs: 'additional keyword-only arguments'
            ) -> str:
        """ does something
        or other""" 
        pass


print(inspect.signature(my_func))

print(type(inspect.signature(my_func)))

sig = inspect.signature(my_func)

print(dir(sig))

for param_name, param in sig.parameters.items():
    print(param_name, param)

def print_info(f: "callable") -> None:
    print(f.__name__)
    print('=' * len(f.__name__), end='\n\n')

    print('{0}\n{1}\n'.format(inspect.getcomments(f), inspect.cleandoc(f.__doc__)))

    print('{0}\n{1}\n'.format('Inputs', '-' * len('Inputs')))

    sig = inspect.signature(f)
    for param in sig.parameters.values():
        print('Name:', param.name)
        print('Default:', param.default)
        print('Annotation:', param.annotation)
        print('Kind:', param.kind)
        print('-----------------------------------\n')
    
    print('{0}\n{1}'.format('\n\nOutput:', '-' * len('Output')))
    print(sig.return_annotation)

print_info(my_func)

## A side note on Positional only Arguments ##

print(help(divmod))

print(divmod(10, 3))

# print(divmod(x=10, y=3)) #error




