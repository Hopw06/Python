from html import escape

def html_escape(arg):
    return escape(str(arg))

def html_int(a):
    return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))

def html_real(a):
    return '{0:.2f}'.format(round(a, 2))

def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')

def html_list(l):
    items = ('<li>{0}</li>'.format(html_escape(item)) for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

def html_dict(d):
    items = ('<li>{0}={1}</li>'.format(html_escape(k), html_escape(v)) for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print(html_str("""this is
a multi line string
with special characters: 10 < 100"""))

print(html_int(255))

print(html_escape(3 + 10j))


# Ideally we would want to just have to call a single function, maybe htmlize that would figure out which particular flavor of the html_xxx function to call depending on the argument type.
# We could try it as follows:

from decimal import Decimal

def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    else:
        return html_escape(str(arg))

print(htmlize([1, 2, 3]))
print(htmlize(dict(key1=1, key2=2, key3=3)))
print(htmlize(255))
print(htmlize(["""first element is
a multi-line string""", [1, 2, 3]]))

# As you can see, the multi-line string did not get the newline characters replaced, the tuple was not rendered as an html list, and the integers do not have their hex representation.

# So we just need to redefine the html_list and html_dict functions to use the htmlize function:

def html_list(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

def html_dict(d):
    items = ['<li>{0}={1}</li>'.format(html_escape(k), htmlize(v)) for k, v in d.items()]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print(htmlize(["""first element is
a multi-line string""", (1, 2, 3)]))

# But we still have something undesirable. You'll notice that the dispatch function htmlize needs to have this big if...elif...else statement that will just keep growing as we need to handle more and more types (including potentially custom types).
# So instead, we are going to try a more flexible approach using decorators.

def singledispatch(fn):
    registry = dict()
    registry[object] = fn

    def inner(arg):
        return registry[object](arg)
    
    return inner

@singledispatch
def htmlizer(arg):
    return escape(str(arg))

print(htmlizer('a < 10'))

def singledispatch(fn):
    registry = dict()

    registry[object] = fn 
    registry[int] = lambda arg: '{0}(<i>{1}</i>)'.format(arg, str(hex(arg)))
    registry[float] = lambda arg: '{0:.2f}'.format(round(arg, 2))

    def inner(arg):
        fn = registry.get(type(arg), registry[object])
        return fn(arg)
    return inner

@singledispatch
def htmlizer(a):
    return escape(a)

print(htmlizer(10))
print(htmlizer(3.1415))

# but this way, we have to modify our decorator to support other object types.
# better:

def singledispatch(fn):
    registry = dict()

    registry[object] = fn

    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn
        return inner
    
    def decorator(arg):
        fn = registry.get(type(arg), registry[object])
        return fn(arg)
    
    def dispatch(type_):
        return registry.get(type_, registry[object])
    
    decorator.register = register
    decorator.registry = registry.keys()
    decorator.dispatch = dispatch
    return decorator

@singledispatch
def htmlizer(arg):
    return escape(str(arg))

print(htmlizer.register)
print(htmlizer.registry)
print(htmlizer.dispatch(str))


@htmlizer.register(int)
def html_int(arg):
    return '{0}(<i>{1}</i>)'.format(arg, str(hex(arg)))

print(htmlizer.registry)
print(htmlizer.dispatch(int))

print(htmlizer(100))

# The huge advantage now is that we can keep registering new handlers from anywhere in our module, or even from outside our module!
@htmlizer.register(float)
def html_real(a):
    return '{0:.2f}'.format(round(a, 2))

@htmlizer.register(str)
def html_str(s):
    return escape(s).replace('\n', '<br/>\n')

@htmlizer.register(tuple)
@htmlizer.register(list)
def html_list(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

@htmlizer.register(dict)
def html_dict(d):
    items = ['<li>{0}={1}</li>'.format(htmlize(k), htmlize(v)) for k, v in d.items()]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print(htmlizer.registry)

print(htmlizer([1, 2, 3]))
print(htmlizer((1, 2, 3)))
print(htmlizer("""this
is a multi line string with
a < 10"""))

# Our single dispatch decorator works quite well - but it has some limitations. For example it cannot handle functions that take in more than one argument (in which case dispatching would be based on the type of the first argument), and we also are not allowing for types based on parent classes - for example, integers and booleans are both integral numbers - i.e. they both inherit from the Integral base class. Similarly lists and tuples are both more generic Sequence types. We'll see this in more detail when we get to the topic of abstract base classes (ABC's).
from numbers import Integral

print(isinstance(100, Integral))
print(isinstance(True, Integral))
print(isinstance(100.5, Integral))
print(type(100) is Integral)
print(type(True) is Integral)

print((100).__class__)
print((True).__class__)

# We can solve this problem by using a built-in decorator from functools

from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence

# The singledispatch returned closure has a few attributes we can use:

# 1. A register decorator (just like ours did)
# 2. A registry property that is the registry dictionary
# 3. A dispatch function that can be used to determine which registry key (registered type) it will use for the specified type.

@singledispatch
def htmlize(a):
    return escape(str(a))

@htmlize.register(Integral)
def htmlize_int(a):
    return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))

print(htmlize.dispatch(int))
print(htmlize.dispatch(bool))

print(htmlize(100))
print(htmlize(True))

@htmlize.register(Sequence)
def html_sequence(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print(htmlize.dispatch(list))
print(htmlize.dispatch(tuple))
print(htmlize.dispatch(str))
# print(htmlize('abc'))