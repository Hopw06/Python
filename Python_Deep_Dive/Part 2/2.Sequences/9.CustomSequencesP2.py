class MyClass:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'MyClass(name={self.name})'
    
    def __add__(self, other):
        return MyClass(self.name + ' ' + other.name)
    
    def __iadd__(self, other):
        self.name += ' ' + other.name
        return self
    
    def __mul__(self, n):
        return MyClass(self.name * n)
    
    def __imul__(self, n):
        self.name *= n
        return self
    
    def __rmul__(self, n):
        self.name *= n
        return self
    
    def __contains__(self, value): # in operator
        return value in self.name

c1 = MyClass('Eric')
c2 = MyClass('Idle')

print(c1, id(c1))
print(c2, id(c2))

c3 = c1 + c2
print(c3, id(c3))

c1 += c2
print(c1, id(c1))

c1 = MyClass('Eric')
print(c1, id(c1))

c1 = c1 * 3
print(c1, id(c1))

c1 *= 4
print(c1, id(c1))

print(2 * c1) # rmul

print("Eric" in c1)