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

x = arr1d(0, 3)
y = arr1d(0, 3)
d = arr1d(0, 3)

for i in range(3):
    x[i], y[i], d[i] = intsput()

intersections = []
for i in range(3):
    for j in range(i+1, 3):
        dx = x[j] - x[i]
        dy = y[j] - y[i]
        dr = math.sqrt(dx**2 + dy**2)
        D = (d[i] - d[j] + dr**2) / (2 * dr**2)
        a = math.sqrt(d[i] - D**2 * dr**2)
        xint = x[i] + D * dx - a * dy / dr
        yint = y[i] + D * dy + a * dx / dr

        intersections.append((xint, yint))

distances = []
for i in range(2):
    dx = x[2] - intersections[i][0]
    dy = y[2] - intersections[i][1]
    distances.append(math.sqrt(dx**2 + dy**2))

if math.isclose(distances[0], math.sqrt(d[2])):
    xfinal, yfinal = intersections[0]
else:
    xfinal, yfinal = intersections[1]

print(int(xfinal), int(yfinal))
