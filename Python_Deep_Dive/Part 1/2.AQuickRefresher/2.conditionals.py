# if else statement
a = 2
if a < 3:
    print("a < 3")
else:
    print("a >= 3")

# nested if statements
a = 15
if a < 5:
    print("a < 5")
elif a < 10:
    if a < 10:
        print("5 <= a < 10")
else:
    print("a >= 10")

# but elif statement provides far better readabillity:


# Python also provides a conditional expression:
# X if (condition) else Y
a = 5
res = 'a < 10' if a < 10 else 'a >= 10'
print(res)

# Note that X and Y can be any expression, not just literal values:
def say_hello():
    print("Hello!")

def say_goodbye():
    print("goodbye")

say_hello() if a < 10 else say_goodbye()

a = 15
say_hello() if a < 10 else say_goodbye()