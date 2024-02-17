import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    x = list(map(int, list(input())[:-1]))
    while len(x) != 1:
        x = list(map(int, list(str(sum(x)))))
    print(x[0])