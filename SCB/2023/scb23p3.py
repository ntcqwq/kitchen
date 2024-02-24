from collections import defaultdict
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
if K > N: K = N+(K-N)%2
food = list(map(int, input().split()))
cmin, cmax = [], []
for i in food:
    cmin.append(str(i))
    cmax.append(str(i))

cmax.sort(key=lambda x: int(x)-int(x[::-1]))
cmin.sort(key=lambda x: int(x)-int(x[::-1]), reverse=True)
cm1, cm2, cm3, cm4, over1, over2 = 0, 0, 0, 0, 0, 0
for i in range(N):
    if not over1:
        if int(cmin[i])-int(cmin[i][::-1]) >= 0:
            cm1 += int(cmin[i][::-1])
            cm2 += int(cmin[i][::-1])
        else:
            lf = K-i
            if lf % 2:
                cm1 += int(cmin[i])
                cm2 += int(cmin[i])
                over1 = 1
            else:
                cm1 += int(cmin[i][::-1])
                cm2 += int(cmin[i])
                if i != 0:
                    cm2 -= int(cmin[i-1][::-1])
                    cm2 += int(cmin[i-1])
                over1 = 1
    else:
        cm1 += int(cmin[i])
        cm2 += int(cmin[i])
    if not over2:
        if int(cmax[i])-int(cmax[i][::-1]) <= 0:
            cm3 += int(cmax[i][::-1])
            cm4 += int(cmax[i][::-1])
        else:
            lf = K-i
            if lf % 2:
                cm3 += int(cmax[i])
                cm4 += int(cmax[i])
                over2 = 1
            else:
                cm3 += int(cmax[i][::-1])
                cm4 += int(cmax[i])
                if i != 0:
                    cm4 -= int(cmax[i-1][::-1])
                    cm4 += int(cmax[i-1])
                over2 = 1
    else:
        cm3 += int(cmax[i])
        cm4 += int(cmax[i])
    print(cm1, cm2, cm3, cm4)
    if K == i+1:
        over1 = 1
        over2 = 1
print(min(cm1, cm2), max(cm3, cm4))
