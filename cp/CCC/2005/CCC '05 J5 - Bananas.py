# https://dmoj.ca/problem/ccc05j5
# 40/40 Python 3

while 1:
    b = input()
    if b == "X":
        break
    while "ANA" in b or "BAS" in b:
        b = b.replace("ANA","A")
        b = b.replace("BAS","A")
    print("YES" if b == "A" else "NO")