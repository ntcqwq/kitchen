from collections import deque, defaultdict 
from bisect import bisect_left as bs, bisect_right as bsr
import sys, math, heapq as hq
input, inf, mx, mod = sys.stdin.readline, int(1e18), 102, 1000000007
# sys.setrecursionlimit(100000)

N, M, R, C = map(int, input().split())
if R == 1 and C == 1:
    print('b'*M)
    for _ in range(N-1):
        print('b'+'a'*(M-1))
else:
    if R == 2 and C == 2:
        print('bb')
        print('bb')
    elif (R == 1 and C == 2) or (R == 2 and C == 1):
        print("IMPOSSIBLE")
    elif R == 1 and C == 1:
        print('ba')
        print('bb')
    elif R == 1 and C == 0:
        print('bb')
        print('ac')
    elif C == 1 and R == 0:
        print('ba')
        print('bc')
    elif C == 0 and R == 0:
        print('ab')
        print('cd')
    elif C == 2 and R == 0:
        print('cb')
        print('cb')
    elif C == 0 and R == 2:
        print('aa')
        print('bb')
    else:
        print(R, C)