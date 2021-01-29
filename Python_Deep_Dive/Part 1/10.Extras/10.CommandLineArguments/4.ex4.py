import sys

for i in range(1, len(sys.argv), 2):
    print(sys.argv[i], sys.argv[i + 1])

# something like: python example4.py --last-name Cleese --first-name John
