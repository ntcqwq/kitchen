f = int(input())
s = int(input())
n = [f, s]
t = 2
while 1:
    t += 1
    ne = n[-2] - n[-1]
    if ne > n[-1]:
        break
    n.append(ne)
print(t)
