import re
instruction = input()
i = re.split('(\d+)', instruction)[:-1]
ip = list(zip(i[::2], i[1::2]))
for pair in ip:
    print(f'{"".join(list(pair[0].replace("+", " tighten ").replace("-", " loosen ")))}{"".join(pair[1])}')
