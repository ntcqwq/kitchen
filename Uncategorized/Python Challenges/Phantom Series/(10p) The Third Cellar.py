import sys

input = sys.stdin.readline

def Sieve(size):
    sieve = [False, False] + [True] * (size-1)
    for i in range(2, size-1):
        if sieve[i] == True:
            for j in range(i+i, len(sieve), i):
                sieve[j] = False
    return sieve
sieve = Sieve(1000000)
for i in range(int(input())):
    a, b = map(int, input().split())
    print(sieve[a:b].count(True))