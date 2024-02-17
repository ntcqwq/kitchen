from collections import deque, defaultdict as dd
from bisect import bisect_left as bs
import sys, math, heapq as hq, itertools, copy
input, inf, mx = sys.stdin.readline, 1e30, int(1e6)+2 
# sys.setrecursionlimit(100000)

N, Q = map(int, input().split())
a = list(map(int, input().split()))