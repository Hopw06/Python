# Question: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9
sentence = input()
numUpperLetter = 0
numLowerLetter = 0
for c in sentence:
    if c.isalpha():
        if c.isupper():
            numUpperLetter += 1
        else:
            numLowerLetter += 1

print('UPPER CASE {0} LOWER CASE {1}'.format(numUpperLetter, numLowerLetter))