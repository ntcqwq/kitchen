# https://dmoj.ca/problem/ccc13s5

import math

N = int(input())

cost = 0
while N > 1:
    r = int(math.sqrt(N)) + 1
    f = 2
    while f <= r and N % f != 0: 
        f += 1    
    if f < N and N % f == 0: 
        x = N / f
        N -= x
        cost += N / x 
    else:                  
        N = N - 1
        cost += N
print(int(cost))
