from functools import lru_cache

class Fib:
    def __init__(self, n):
        self._n = n

    @lru_cache(maxsize=1000)
    def _fib(self, n):
        return 1 if n < 3 else self._fib(n - 1) + self._fib(n - 2)

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0:
                s = s + self._n
            if s < 0 or s >= self._n:
                raise IndexError
            return self._fib(s)
        else:
            idx = s.indices(self._n)
            rng = range(idx[0], idx[1], idx[2])
            return [self._fib(n) for n in rng]

    def __len__(self):
        return self._n

fib = Fib(10)

print(len(fib))

print(fib[9])

for x in fib:
    print(x)

print(fib[1:10])
print(fib[::-1])