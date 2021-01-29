_sentinel = object()

def validate(a=_sentinel):
    if a is not _sentinel:
        print('Argument was provided')
    else:
        print('Argument was not provided')

validate(100)

validate(None)

validate(object())

validate()

# the other way
def validate(a=object()):
    default_a = validate.__defaults__[0]
    if a is not default_a:
        print('Argument was provided')
    else:
        print('Argument was not provided')

validate(100)

validate(None)

validate(object())

validate()

# We can expand this to several parameters as well if we need to