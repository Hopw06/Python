class Squares:
    def __init__(self, n):
        self._n = n
    
    def __len__(self):
        return self._n
    
    def __getitem__(self, i):
        print("Calling getitem...")
        if i >= self._n:
            raise IndexError
        else:
            return i ** 2

sq = Squares(5)

for i in sq:
    print(i)

sq_iter = iter(sq)

print(type(sq_iter))

while True:
    try:
        print(next(sq_iter))
    except StopIteration:
        print("Stop exception")
        break

# Python will first try to get the iterator by invoking the __iter__ method on our object.
# Here's how we might build an iterator:

class Squares:
    def __init__(self, n):
        self._n = n
    
    def __getitem__(self, i):
        if i >= self._n:
            raise IndexError
        else:
            return i ** 2

class SquaresIterator:
    def __init__(self, squares):
        self._squares = squares
        self._i = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        print("Calling next in iterator")
        try:
            result = self._squares[self._i]
            self._i += 1
            return result
        except IndexError:
            raise StopIteration()

sq_iterator = SquaresIterator(sq)

for i in sq_iterator:
    print(i)

# How to test if an object is iterable
class SimpleIter:
    def __init__(self):
        pass

    def __iter__(self):
        return 'Nope'

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

print(is_iterable(SimpleIter()))
print(is_iterable(Squares(5)))