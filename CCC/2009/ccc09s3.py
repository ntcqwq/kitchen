import sys, collections

n = [set(), {6}, {6}, {4, 5, 6, 15}, {3, 5, 6}, {3, 4, 6},
           {1, 2, 3, 4, 5, 7}, {6, 8}, {7, 9}, {8, 10, 12}, {9, 11},
           {10, 12}, {9, 11, 13}, {12, 14, 15}, {13}, {3, 13}, {17, 18},
           {16, 18}, {16, 17}, set(), set(), set(), set(), set(), set(),
           set(), set(), set(), set(), set(), set(), set(), set(), set(),
           set(), set(), set(), set(), set(), set(), set(), set(), set(),
           set(), set(), set(), set(), set(), set(), set(), set()];

ins = input()
while ins != 'q':
    x = int(input());
    if ins == 'i':
        y = int(input())
        n[x].add(y);
        n[y].add(x);
    elif ins == 'd':
        y = int(input());
        n[x].remove(y);
        n[y].remove(x);
    elif ins == 'n':
        print(len(n[x]));
    elif ins == 'f':
        ffs = set();
        for y in n[x]:
            ffs = ffs.union(n[y]);
        for y in n[x]:
            if y in ffs:
                ffs.remove(y);
        if x in ffs:
            ffs.remove(x);
        print(len(ffs));
    elif ins == 's':
        y = int(input())
        dis = [-1]*50
        q = collections.deque([])
        q.append(x)
        dis[x] = 0
        shortest = float('inf')
        while q:
            cur = q.popleft()
            for nxt in n[cur]:
                if dis[nxt] == -1:
                    q.append(nxt)
                    dis[nxt] = dis[cur] + 1;
                    if nxt == y:
                        shortest = dis[nxt]
                        break
        if shortest != float('inf'):
            print(shortest)
        else:
            print("Not connected")
    ins = input();