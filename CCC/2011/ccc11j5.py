import sys
input = sys.stdin.readline

N = int(input())
ways = [1]*8
for i in range(1, N):
    ways[int(input())] *= (1 + ways[i])
print(ways[N])