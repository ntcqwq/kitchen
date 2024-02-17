import sys
input = sys.stdin.readline
m, n, k = int(input()), int(input()), int(input())
rows, cols = [0 for x in range(m)], [0 for y in range(n)]
for _ in range(k):
    order = input().split()
    index = int(order[1])-1
    if order[0] == "R":
        rows[index] = rows[index]^1
    else:
        cols[index] = cols[index]^1
count = 0
for row in range(m):
    for col in range(n):
        count += (1 if rows[row] + cols[col] == 1 else 0)
print(count)