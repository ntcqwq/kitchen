INF = float('inf')
f = input()
K = eval(f)
lights = []
for i in range(0,K):
    lights.append(eval(input()))
group = []
N = 0
group.append ([0, 0])

for i  in range (0, K):
    if lights[i] == 1:
        if group[N][1] == 0:
            group[N][0] = i
            group[N][1] = i
        group[N][1] = group[N][1] + 1
    elif group[N][1] != 0:
        N = N + 1
        group.append ([0, 0])
        
if group[N][1] == 0:
    N = N - 1
    group.pop()

N = N + 1
minimumSwitches = []
for i in range(0,N+1):
    minimumSwitches.append (0)
numL = 0
for i in range(N-1, -1, -1):
    minimumSwitches[i] = INF;
    numOnes = 0;
    j = i
    while j < N and ((group[j][1] - group[i][0]) <= 7):
        numOnes = numOnes + group[j][1] - group[j][0]
        len = max(4, group[j][1] - group[i][0]);
        t = len - numOnes
        if len == 6 and lights[group[i][0] + 2] == 1 and lights[group[i][0] + 3] == 1:
            t = INF
        elif len == 7 and lights[group[i][0] + 3] == 1:
            t = INF
        minimumSwitches[i] = min(minimumSwitches[i], t + minimumSwitches[j+1])
        j = j + 1
print(minimumSwitches[0])