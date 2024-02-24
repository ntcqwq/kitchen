from collections import defaultdict
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
food = list(map(int, input().split()))
cmin = cmax = []
for i in food:
    cmin.append(str(i))
    cmax.append(str(i))

cmax.sort(key=lambda x: int(x)-int(x[::-1]))
cmin.sort(key=lambda x: int(x)-int(x[::-1]), reverse=True)

cm1 = cm2 = cm3 = cm4 = 0
if K <= N:
    for i in range(K):
        if int(cmin[i])-int(cmin[i][::-1]) <= 0:
            cm1 += int(cmin[i][::-1])
            cm2 += int(cmin[i][::-1])
        else:
            lf = K-i
            
        if int(cmin[i])-int(cmin[i][::-1]) >= 0:
            cm3 += int(cmin[i][::-1])
            cm4 += int(cmin[i][::-1])
        else:

else:
    l = K-N
    K = N-1 if l % 2 else N
    for i in range(K):
        cmin[i] = cmin[i][::-1]
        cmax[i] = cmax[i][::-1]
print(sum(list(map(int, cmin))), sum(list(map(int, cmax))))
