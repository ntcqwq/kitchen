import math, sys
input = sys.stdin.readline
for i in range(int(input())):
    f = int(input())
    if f <= 33: 
        print(math.factorial(f)%2**32)
    else: 
        print(0)