M = int(input())
maxTime = int(M%720)
h = int(maxTime/60)
m = int(maxTime%60)
maxHour = int((12 + h)%12)
maxMinute = int((0 + m)%60)
times = {
    12: [34],
    1: [11, 23, 35, 47, 59],
    2: [10, 22, 34, 46, 58],
    3: [21, 33, 45, 57],
    4: [32, 20, 44, 56],
    5: [31, 43, 55],
    6: [54, 42, 30],
    7: [53, 41],
    8: [52, 40],
    9: [51],
    10: [],
    11: [11]
}
total = int(M/720)*31
for hour in times:
    if maxHour > hour or hour == 12:
        total += len(times[hour])
    elif maxHour == hour:
        for minute in times[hour]:
            if maxMinute >= minute:
                total += 1
    else:
        break
if M == 0:
    print(0)
else:
    print(total)