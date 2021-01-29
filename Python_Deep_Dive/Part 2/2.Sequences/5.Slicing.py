s = slice(0, 2)
print(type(s))
print(s.start)
print(s.stop)

l = [1, 2, 3, 4, 5]
print(l[s])

data = []
for row in data:
    first_name = row[0:51]
    last_name = row[51:101]
    ssn = row[101:111]

# instead, you might write:
range_first_name = slice(0, 51)
range_last_name = slice(51, 101)
range_ssn = slice(101, 111)

for row in data:
    first_name = row[range_first_name]
    last_name = row[range_last_name]
    ssn = row[range_ssn]

## Slice Fundamentals ##
l = 'python'

print(l[0:1], l[0:6])
print(l[0:6:2], l[0:6:3])

s1 = slice(0, 6, 2)
s2 = slice(0, 6, 3)
print(l[s1], l[s2])

print(l[6:0:-1])
print(l[::-1])