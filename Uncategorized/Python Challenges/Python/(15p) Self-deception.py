# https://dmoj.ca/problem/python1
# 100/100 Python 2

def call_magic_method():
    magic = Magic()
    magic.method.__func__(None)

call_magic_method()