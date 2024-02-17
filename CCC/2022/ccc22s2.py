import sys
input = sys.stdin.readline

X = int(input())
xdata = {}
for i in range(X):
    n1, n2 = input().split()
    if not n1 in xdata:
        xdata[n1] = [n2]
    else:
        xdata[n1].append(n2)

Y = int(input())
ydata = {}
for i in range(Y):
    n1, n2 = input().split()
    if not n1 in ydata:
        ydata[n1] = [n2]
    else:
        ydata[n1].append(n2)

violations = 0
G = int(input())
for _ in range(G):
    group = input().split()
    for i in group:
        if i in xdata:
            for x in xdata[i]:
                if x not in group:
                    violations += 1
        if i in ydata:
            for y in ydata[i]:
                if y in group:
                    violations += 1

print(violations)