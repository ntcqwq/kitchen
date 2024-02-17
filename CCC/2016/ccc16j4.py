h, m = input().split(":")
h, m = int(h), int(m)

distanceTime = 0.0

while distanceTime < 120:
    m += 1

    if 6 < h < 10:
        distanceTime += 0.5
    elif 14 < h < 19:
        distanceTime += 0.5
    else:
        distanceTime += 1

    if m == 60:
        if h == 23:
            h = 0
        else:
            h += 1
        m = 0


if m < 10:
    if h < 10:
        print("0" + str(h) + ":" + "0" + str(m))
    else:
        print(str(h) + ":" + "0" + str(m))
else:
    if h < 10:
        print("0" + str(h) + ":" + str(m))
    else:
        print(str(h) + ":" + str(m))