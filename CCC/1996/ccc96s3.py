import sys, itertools
input = sys.stdin.readline

N = int(input())
for i in range(N):
    n, k = map(int, input().strip().split())
    b = "1" * k + "0" * (n - k)
    print("The bit patterns are")
    while True:
        print(b)
        insert = b.rfind("10")
        b = b[:insert] + "01" + b[insert+2:][::-1] 
        if len(b) > n:
            break
    if i != N-1:
        print()