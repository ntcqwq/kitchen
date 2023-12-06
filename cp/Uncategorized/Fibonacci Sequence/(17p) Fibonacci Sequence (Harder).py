# Solution by d
# 100/100 py3

m = 1000000007
period = 2*m+2
n = 0
for ch in input().strip():
    n = (n*10+int(ch))%period
n += period-1
temp = (1,1,0)
out = (1,1,0)
while n!=0:
    if n%2==1:
        out = ((out[0]*temp[0]+out[1]*temp[1])%m,(out[0]*temp[1]+out[1]*temp[2])%m,(out[1]*temp[1]+out[2]*temp[2])%m)
    temp = ((temp[0]**2+temp[1]**2)%m,(temp[0]*temp[1]+temp[1]*temp[2])%m,(temp[1]**2+temp[2]**2)%m)
    n //= 2
print(out[1])
