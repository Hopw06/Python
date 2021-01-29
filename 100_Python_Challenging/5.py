# Question: Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case. Also please include simple test function to test the class methods.
class SimpleString:

    def __init__(self):
        self.input = ""
    
    def getString(self):
        self.input = input()

    def printString(self):
        print(self.input.upper())

simple_string = SimpleString()
simple_string.getString()
simple_string.printString()