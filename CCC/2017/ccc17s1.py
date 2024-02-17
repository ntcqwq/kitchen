K = int(input())
Sw = list(map(int, input().split()))
Se = list(map(int, input().split()))

SwS = 0
SeS = 0
l = 0

for i in range(K):
    SwS += Sw[i]
    SeS += Se[i]
    if SwS == SeS:
        l = i+1

print(l)