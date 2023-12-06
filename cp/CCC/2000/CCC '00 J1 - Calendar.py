info = input()
i_space = info.find(' ')

start_on = int(info[:i_space])
num_days = int(info[i_space + 1:])

days = ('Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat')
for d in days:
    if d == 'Sat':
        print(d, end='')
    else:
        print(d, end=' ')

preceding_space = start_on * 4 - 5

if start_on == 1:
    print('\n' + preceding_space * ' ', end=2 * ' ')
else:
    print('\n' + preceding_space * ' ', end=3 * ' ')

day_at_end = 8 - start_on
row_num = 0

for d in range(1, num_days + 1):
    if d == num_days:
        print(d, end='')

    else:
        if d % (day_at_end + 7 * row_num) == 0:
            print(d)
            if d < 9:
                print(2 * ' ', end='')
            else:
                print(' ', end='')
            row_num += 1

        else:
            if d < 9:
                print(d, end=3 * ' ')
            else:
                print(d, end=2 * ' ')

print()