sqr, crcl = map(int, input().split())
print("SQUARE" if sqr**2 > crcl**2*3.14 else "CIRCLE")