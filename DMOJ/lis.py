from collections import deque; from bisect import bisect_left as bs; import sys, math, heapq as hq;
input, inf = sys.stdin.readline, float('inf')
# sys.setrecursionlimit(100000)

N = int(input())
lis = []
a = list(map(int, input().split()))
for i in range(N):
    x = a[i]
    if not lis or x > lis[-1]:
        lis.append(x)
    else:
        lis[bs(lis, x)] = x
print(len(lis))