import re

line = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('@([^ ]*)', line)
print(y)

y = re.findall('@(\S+)', line)
print(y)

y = re.findall('^From .*@([^ ]*)', line)
print(y)

x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)