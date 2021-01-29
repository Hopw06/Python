import sys

print(sys.argv)

# try running this script as follows:
# python example1.py 123 hello 456 goodbye
# Output:
# ['example1.py', '123', 'hello', '456', 'goodbye']

# now try running it this way:
# python example1.py [1, 2, 3] [4, 5, 6]
# Output:
# ['example1.py', '[1,', '2,', '3]', '[4,', '5,', '6]']

# or even this example:
# python example1.py --name John --years 1980 1981 1982
# Output:
# ['example1.py', '--name', 'John', '--years', '1980', '1981', '1982']