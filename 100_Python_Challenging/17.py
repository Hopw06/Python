# Question: Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following: D 100 W 200

# D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500
logs = input().split(' ')
n = len(logs)
net = 0
for i in range(0, n - 1, 2):
    if logs[i] == 'D':
        net += int(logs[i + 1])
    else:
        net -= int(logs[i + 1])
print(net)