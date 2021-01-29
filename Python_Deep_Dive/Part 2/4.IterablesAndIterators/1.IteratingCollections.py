s = {'x', 'y', 'b', 'c', 'a'}
for item in s:
    print(item)

# the order of elements is unknow.

class Squares:
    def __init__(self, length):
        self.length = length
        self.i = 0
    
    def __iter__(self):
        print("calling __iter__")
        self.i = 0
        return self
    
    def __next__(self):
        print("calling __next__")
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result
    
    def __len__(self):
        return self.length

sq = Squares(5)
for i in sq:
    print(i)

for i in sq:
    print(i)
