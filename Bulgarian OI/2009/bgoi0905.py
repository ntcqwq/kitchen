snum = [];

def s7(c: int):
    return int("7" + "0"*c);

def s97(c: int):
    seq = [];
    count = c-1;
    while count != -1:
        seq.append(int("9"*((c-1)-count) + "97" + "0" * count));
        count -= 1;
    return seq;

def s2(c: int):
    seq = [];
    if c == 1:
        return [];
    elif c == 2:
        return [2120]
    else:
        c -= 1
        digits = c + 3;
        nums = c // 2;
        if c % 2 == 0:
            seq.append(int("2" + "0"*int((digits-3)/2) + "1" + "0"*int((digits-3)/2) + "2"));
            for i in range(1, nums):
                seq.append(int("2" + "0"*(int((digits-3)/2)-i) + "1" + "0"*(int((digits-3)/2)-i) + "2" + "0"*(2*i)));
        else:
            seq.append(int("2" + "0"*int((digits-3)/2) + "1" + "0"*int((digits-3)/2) + "2" + "0"));
            for i in range(1, nums):    
                seq.append(int("2" + "0"*(int((digits-3)/2)-i) + "1" + "0"*(int((digits-3)/2)-i) + "20" + "0"*(2*i)));
        seq.append(int("212" + "0" * c));
        return seq;

def s3(c: int):
    seq = [];
    if c == 1:
        return seq
    else:
        if c > 4:
            seq.append(int("3074003" + "0"*(c-5)));
        seq.append(int("3148" + "0"*(c-2)));
        return seq

N = int(input())
cycle = 1
while len(snum) <= N:
    snum.append(s7(cycle))
    snum += s97(cycle)
    snum += s2(cycle)
    snum += s3(cycle)
    cycle += 1

for i in range(0, 5):
    snum.append(953671853653*(10**i))
    snum.append(2118984413357*(10**i))
    snum.append(2121179131852*(10**i))
snum.append(95367185365300000)
snum.append(6328428636000007)
snum.append(63284286360000070)
snum.append(99704560597822753)
snum.sort()

print(snum[N-1])