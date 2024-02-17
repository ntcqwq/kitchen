from collections import deque; from bisect import bisect_left as bs; import sys, math, heapq as hq;
input, inf, mx = sys.stdin.readline, float('inf'), 2010
# sys.setrecursionlimit(100000)

N, K = map(int, input().split())
a = input().strip()
freq = [0]*26
lf = [mx, mx]
for c in a: 
    freq[ord(c)-ord('a')] += 1
for i in range(26):
    if freq[i] < lf[0]: lf = [freq[i], i]
if K > N or K < lf[0]: print("WRONGANSWER")
else:
    b, f = "", chr(lf[1]+ord('a'))
    o, i, fc = K-lf[0], 0, 0
    while o:
        b += a[i]
        if a[i] != f: o -= 1
        else: fc += 1
        i += 1
    b += f*(N-(K-lf[0])-fc)
    print(b)