d = {"MG": "midget girls",
"MB": "midget boys",
"JG": "junior girls",
"JB": "junior boys",
"SG": "senior girls",
"SB": "senior boys"}

N = input()
try:
    print(d[N])
except:
    print("invalid code")