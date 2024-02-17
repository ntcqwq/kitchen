# https://dmoj.ca/problem/python3
# 50/50 py2

def f(n):
    print(n)

code = foo.__code__
cc = type(code)(code.co_argcount,
             code.co_nlocals,
             code.co_stacksize,
             code.co_flags,
             code.co_code,
             tuple([f.__code__ if type(x) == type(code) else x for x in code.co_consts]), 
             code.co_names,
             code.co_varnames,
             code.co_filename,
             'foo',
             code.co_firstlineno,
             code.co_lnotab,
             (),
             (),
             )
type(lambda x : x)(cc, foo.func_globals)()