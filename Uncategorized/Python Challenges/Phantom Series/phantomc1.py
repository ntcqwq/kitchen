print" ".join(`a`+" *"[[b.__setitem__(c,0)for c in b[a*a::a]]>0<b[a-2]|b[a+2]]for b in[range(input())]for a in b if a>1)


