def find_ls(N, reviews):
    ls = 0
    for a in range(1440):
        s = 0
        lda = False
        for t in reviews:
            if (t - a) % 1440 < 2: 
                if lda:
                    s += 1
                else:
                    s = 1
                    lda = True
            elif (t - a) % 1440 >= (1440 - 2):
                if lda:
                    s += 1
                    lda = False
            else: 
                if not lda:
                    s = 1
                    lda = True
                else:
                    s += 1
        if s > ls:
            ls = s
    return ls

N, D = map(int, input().split())
reviews = list(map(int, input().split()))

print(find_ls(N, reviews))
