N = int(input())

for i in range(N):
    a = list((input()))
    count = 0
    val = a[0]
    for j in a:
        if j == val:
            count += 1
        else:
            print(count, val, end=" ")
            val = j
            count = 1
    print(count, val)