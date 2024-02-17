tfl = []
for i in range(1,20001):
    if str(i*i*i)[-3:] == "888":
        tfl.append(i)

t = int(input())
for _ in range(t):
    f = int(input())
    tfl.append(f)
    tfl.sort()
    index = tfl.index(f)
    print(tfl[index+1])
    tfl.remove(f)