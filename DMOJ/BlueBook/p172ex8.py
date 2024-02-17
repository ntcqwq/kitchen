count = [0] * 101
while True:
    N = int(input())
    if N == -1:
        break
    else:
        count[N] += 1

a = []
ans = 0
for i in range(101):
    if count[i] > ans:
        ans = count[i]
        a = []
        a.append(i)
    elif count[i] == ans:
        a.append(i)

print(*a)