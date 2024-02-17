from random import randint

def is_prime(n):
    iterations = 4
    if n < 2:
        return False
    if n in [2,3]:
        return True
    s, d = 0, n-1
    while pow(d, 1, 2) == 0:
        s, d = s+1, d//2
    for i in range(iterations):
        x = pow(randint(2, n-1), d, n)
        if x == 1 or x == n-1:
            continue
        for r in range(1, s):
            x = pow(x*x, 1, n)
            if x == 1:
                return False
            if x == n-1:
                break
        else:
            return False
    return True

m, primes, i, total = int(input()), [], 0, 0
while True:
    if is_prime(i):
        total += 1
        primes.append(i)
    if len(primes) == 10:
        print(*primes)
        primes = []
    i += 1
    if total == m:
        break
if primes: 
    print(*primes)