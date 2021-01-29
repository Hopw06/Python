import itertools

n = 10
iter_cycl = itertools.cycle('NSWE')
lst = [f'{i}{next(iter_cycl)}' for i in range(1, n + 1)]
print(lst)