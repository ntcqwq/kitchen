shelf = input()
large, mid = shelf.count('L'), shelf.count('M')
Ls, Ms = shelf[:large], shelf[large:mid+large]
Ml = Ls.count('M') + Ls.count('S')
Mm = Ms.count('L') + Ms.count('S')
print(Ml + Mm - min(Ls.count('M'),Ms.count('L')))
