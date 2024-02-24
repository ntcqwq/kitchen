from collections import deque, defaultdict; from bisect import bisect_left as bs; import sys, math, heapq as hq, itertools, copy;
input, inf, mx = sys.stdin.readline, 1e30, 102 
# sys.setrecursionlimit(100000)

T = int(input())
for _ in range(T):
    N = int(input())
    h = list(map(int, input().split()))
    a = set()
    for i in range(1, N):
        if h[i] == h[i-1]:
            a.add(h[i])
        elif i >= 2 and h[i] == h[i-2]:
            a.add(h[i])
    if not len(a):
        print(-1)
    else:
        print(*sorted(a))