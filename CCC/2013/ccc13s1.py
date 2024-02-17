c = int(input())
i = c
while 1:
    if len(set(str(i))) == len(str(i)):
        if i != c:
            print(i)
            break
    i += 1