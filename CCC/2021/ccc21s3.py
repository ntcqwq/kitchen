from collections import deque
import bisect as bs
import sys, math
import heapq as hq

sys.setrecursionlimit(100000)

input = sys.stdin.readline
inf = float('inf')

# o = open('input.txt', 'r')
# f = open('output.txt', 'w')
# input = o.readline

N = int(input())

pwd = [list(map(int, input().split())) for _ in range(N)]
pwd.sort()

lo = pwd[0][0]
hi = pwd[-1][0]
ans = inf

def check(m):
    ret = 0
    for p, w, d in pwd:
        if m > p:
            if m > p + d:
                ret += (m - p - d) * w
        else:
            if m < p - d:
                ret += (p - d - m) * w
    return ret

while lo <= hi:
    mid = (lo + hi) // 2
    if check(mid) < check(mid+1):
        hi = mid - 1
        ans = mid
    else:
        lo = mid + 1

ans = check(ans)
print(ans)