class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __call__(self, fn):
        def inner(*args, **kwargs):
            print('MyClass instance called: a={0}, b={1}'.format(self.a, self.b))
            return fn(*args, **kwargs)
        return inner
    
@MyClass(10, 20) # more specific: my_func = MyClass(10, 20)(my_func)
def my_func(s):
    print('Hello {0}!'.format(s))

my_func('Python')