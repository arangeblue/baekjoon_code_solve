import sys

M = int(sys.stdin.readline())

if M == 1:
    print("")

for i in range(2, M+1):
    if M%i ==0:
        while M % i == 0:
            print(i)
            M = M / i