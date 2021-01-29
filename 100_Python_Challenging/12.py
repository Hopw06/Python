# Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.
def isAllDigitsEven(num):
    while num:
        num, rm = divmod(num, 10)
        if rm & 1:
            return False
    return True

rs = []
for i in range(1000, 3000):
    if isAllDigitsEven(i):
        rs.append(str(i))

print(','.join(rs))

# Solution from zhiwehu, I think it is smart :D. It base on the fact that there are only four digits in those numbers.
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))