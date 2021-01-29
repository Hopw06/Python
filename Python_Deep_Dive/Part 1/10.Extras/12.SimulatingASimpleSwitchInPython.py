def dow_switch_fn(dow):
    if dow == 1:
        fn = lambda: print('Monday')
    elif dow == 2:
        fn = lambda: print('Tuesday')
    elif dow == 3:
        fn = lambda: print('Wednesday')
    elif dow == 4:
        fn = lambda: print('Thursday')
    elif dow == 5:
        fn = lambda: print('Friday')
    elif dow == 6:
        fn = lambda: print('Saturday')
    elif dow == 7:
        fn = lambda: print('Sunday')
    else:
        fn = lambda: print('Invalid day of week')
    
    return fn()

dow_switch_fn(1)

dow_switch_fn(100)

def dow_switch_dict(dow):
    dow_dict = {
        1: lambda: print('Monday'),
        2: lambda: print('Tuesday'),
        3: lambda: print('Wednesday'),
        4: lambda: print('Thursday'),
        5: lambda: print('Friday'),
        6: lambda: print('Saturday'),
        7: lambda: print('Sunday'),
        'default': lambda: print('Invalid day of week')
    }

    return dow_dict.get(dow, dow_dict['default'])()

dow_switch_dict(1)

dow_switch_dict(100)

# using decorator
def switcher(fn):
    registry = dict()
    registry['default'] = fn

    def register(case):
        def inner(fn):
            registry[case] = fn
            return fn
        return inner
    
    def decorator(case):
        fn = registry.get(case, registry['default'])
        return fn
    
    decorator.register = register
    return decorator

@switcher
def dow():
    print('Invalid day of week')

@dow.register(1)
def dow_1():
    print('Monday')

dow.register(2)(lambda: print('Tuesday'))
dow.register(3)(lambda: print('Wednesday'))
dow.register(4)(lambda: print('Thursday'))
dow.register(5)(lambda: print('Friday'))
dow.register(6)(lambda: print('Saturday'))
dow.register(7)(lambda: print('Sunday'))

dow(1)()

dow(2)()

dow(100)()