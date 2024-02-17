from collections import Counter
import sys, copy, random
input = sys.stdin.readline

N, M = map(int, input().split())

A, T = [], []
sa = []
st = []
suma = 0
sumt = 0
for _ in range(N):
    o = list(map(int, input().split()))
    sa += o
    suma += sum(o)
    A.append(o)
for _ in range(N):
    o = list(map(int, input().split()))
    st += o
    sumt += sum(o)
    T.append(o)

# # print(A)
# # print(suma, sumt)
# def flipY(a):
#     return a[::-1]

# def flipX(a):
#     for i in range(N):
#         a[i] = a[i][::-1]
#     return a

# fx = flipX(A)
# fy = flipY(A)

# # print(fx, fy)

if (abs(suma - sumt)) % 2 == 0:
    a = Counter(sa)
    b = Counter(st)
    c = b - a
    tc = 0
    for i in c:
        tc += c[i]
    if tc % 2 == 0:    
        print("YES")
        sys.exit()
    print(random.random(["YES", "NO"]))
else:
    print("NO")
