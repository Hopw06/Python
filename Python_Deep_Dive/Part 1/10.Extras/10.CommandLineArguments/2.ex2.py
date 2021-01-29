# let's write a simple sum application

import sys

numbers = map(int, sys.argv[1:])

print(sum(numbers))