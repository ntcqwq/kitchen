import sys, collections, math, bisect, itertools

lineput = lambda: sys.stdin.readline().strip()
intput = lambda: int(sys.stdin.readline())
allput = lambda: sys.stdin.read().split('\n')
intsput = lambda: map(int, lineput().split())
stringsput = lambda: lineput().strip().split()
printf = lambda x: sys.stdout.write("%d\n" % x)  # Annotate when py2
prints = lambda x: sys.stdout.write(x)
printeach = lambda x, y = "": print(*x, sep=y)  # Annotate when py2 
arr1d = lambda x, y: [x] * y 
arr2d = lambda x, y, i: [[i for _ in range(x)] for _ in range(y)]
fill = lambda x: list(range(0, x + 1))
flat = lambda x, l: x.join(map(str, l)) 
mat, mit, MOD = sys.maxsize, -sys.maxsize, int(1e9 + 7)
flush = sys.stdout.flush()
perm = lambda x: itertools.permutations(x)
# printline = lambda x: list(map(print, x))
# sys.setrecursionlimit(1000000)  # if pypy3 MLE

N, M = intsput()
graph = {i: [] for i in range(N)}

for i in range(M):
    a, b = intsput()
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

frts = []
for i in range(N):
    for j in graph[i]:
        for k in graph[j]:
            if i != k and i in graph[k]:
                frts.append(frozenset((i, j, k)))

bowties = set()
for i in range(len(frts)):
    for j in range(i+1, len(frts)):
        shared = frts[i] & frts[j]
        if len(shared) == 1:
            bowties.add(frozenset((frts[i], frts[j])))

printf(len(bowties))



