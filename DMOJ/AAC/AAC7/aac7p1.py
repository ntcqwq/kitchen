N = int(input())
for _ in range(N):
    a,b=map(int,input().split())
    if (a<4 and b<4) or (a==1) or (a<7 and b==1):
        print("bad")
    else:
        print("good")