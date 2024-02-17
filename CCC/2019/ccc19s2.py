import random, sys
input = sys.stdin.readline

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(30):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
    
T = int(input())

for _ in range(T):
    N = int(input().strip())
    if isPrime(N):
        print(N, N)
    else:
        for i in range(2, 2*N):
            A, B = i, 2*N - i

            if isPrime(A) and isPrime(B):
                if 2 * N == A + B:
                    print(A, B)
                    break