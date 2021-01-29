## **kwargs ##
def func(**kwargs):
    print(kwargs)

func(x=100, y=200)

def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, 3, x=4, y=5)

# Also, you cannot specify parameters after **kwargs has been used:
# def func(a, b, **kwargs, c):
#     pass

# make sure only Keyword Arguments and kwargs:
def func(*, d, **kwargs):
    print(d)
    print(kwargs)

func(d=10, a=1, b=2, c=3)