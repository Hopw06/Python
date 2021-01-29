## sorted function ##
l = ['a', 'B', 'c', 'D']
print(sorted(l))

# We can custome the sorted function the way we want:
print(sorted(l, key=str.upper))

# Or lambda
print(sorted(l, key=lambda s: s.upper()))

d = {'def': 300, 'abc': 200, 'ghi': 100}

print(d)
print(sorted(d))

print(sorted(d, key=lambda k: d[k]))

def dist(x):
    return (x.real)**2 + (x.imag)**2

l = [3 + 3j, 1 + 1j, 0]

# print(sorted(l)) # error

print(sorted(l, key=dist))
