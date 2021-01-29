# Question: Write a program that accepts a sentence and calculate the number of letters and digits. Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3
import string
numDigits = 0
numLetters = 0
sentence = input()
for c in sentence:
    if c in string.ascii_letters: #isalpha()
        numLetters += 1
    elif c in string.digits: #isdigit()
        numDigits += 1
print('LETTERS {0} DIGITS {1}'.format(numLetters, numDigits))