data = []
for _ in range(6):
    data.append(int(input()))
    
print('A' if data[0]*3+data[1]*2+data[2]>data[3]*3+data[4]*2+data[5] else 'B' if data[0]*3+data[1]*2+data[2]<data[3]*3+data[4]*2+data[5] else 'T')