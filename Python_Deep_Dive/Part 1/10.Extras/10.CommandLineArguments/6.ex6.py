import argparse

parser = argparse.ArgumentParser('Calculates the div a//b and mod a % b of two integer.')
parser.add_argument("a", help="first integer", type=int)
parser.add_argument("b", help="second integer", type=int)

args = parser.parse_args()

a = args.a
b = args.b

print(f'{a}//{b} = {a//b}, {a}%{b} = {a%b}')

# now try running these:
# python example6.py -h
# python example6.py 10 3
# python example6.py 10.5 3