n = int(input())
a = []
for _ in range(n):
    a.append(input())
c = []
for _ in range(n):
    c.append(input())
total = 0
for each in range(len(a)):
    if a[each] == c[each]:
        total += 1
print(total)