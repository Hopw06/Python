## Nonlocal Scopes
# Functions defined inside anther function can reference variables from that enclosing scope, just like functions can reference variables from the global scope.

def outer_func():
    x = 'hello'

    def inner_func():
        print(x)
    
    inner_func()

outer_func()

# In fact, any level of nesting is supported since Python just keeps looking in enclosing scopes until it finds what it needs (or fails to find it by the time it finishes looking in the built-in scope, in which case a runtime error occurrs.)

def outer_func():
    x = 'hello'
    def inner1():
        def inner2():
            print(x)
        inner2()
    inner1()

outer_func()

# In fact, any level of nesting is supported since Python just keeps looking in enclosing scopes until it finds what it needs (or fails to find it by the time it finishes looking in the built-in scope, in which case a runtime error occurrs.)
def outer():
    x = 'hello'
    def inner():
        x = 'python'
    inner()
    print(x)

outer()

# x in outer was not changed.

# We can use nonlocal keyword

def outer():
    x = 'hello'
    def inner():
        nonlocal x
        x = 'python'
    inner()
    print(x)

outer()

def outer():
    x = 'hello'
    def inner1():
        def inner2():
            nonlocal x
            x = 'python'
        inner2()
    inner1()
    print(x)

outer()

# How far Python looks up the chain depends on the first occurrence of the variable name in an enclosing scope.
def outer():
    x = 'hello'
    def inner1():
        x = 'python'
        def inner2():
            nonlocal x
            x = 'monty'
        print('inner1 (before):', x)
        inner2()
        print('inner2 (after):', x)
    inner1()
    print('outer: ', x)

outer()


# What happened here, is that x in inner1 masked x in outer. But inner2 indicated to Python that x was nonlocal, so the first local variable up in the enclosing scope chain Python found was the one in inner1, hence x in inner2 is actually referencing x that is local to inner1
# We can:

def outer():
    x = 'hello'
    def inner1():
        nonlocal x
        x = 'python'
        def inner2():
            nonlocal x
            x = 'monty'
        print('inner1 (before):', x)
        inner2()
        print('inner2 (after):', x)
    inner1()
    print('outer:', x)

outer()

x = 100
def outer():
    x = 'python'
    def inner1():
        nonlocal x
        x = 'monty'
        def inner2():
            global x
            x = 'hello'
        print('inner1 (before):', x)
        inner2()
        print('inner1 (after):', x)
    inner1()
    print('outer', x)

outer()
print(x)

def outer():
    global x
    x = 'python'

    def inner():
        nonlocal x # can not find local variable x.
        x = 'monty' 
    inner()

outer()