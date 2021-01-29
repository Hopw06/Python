import sys


keys = sys.argv[1::2]
values = sys.argv[2::2]

print(keys)
print(values)

args = {k: v for k, v in zip(keys, values)}
print(args)

first_name = args.get('--first-name')
last_name = args.get('--last-name')
print(first_name, last_name)

# python .\5.ex5.py --last-name Cleese --first-name John