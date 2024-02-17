import sys
input = sys.stdin.readline

N = int(input())
book = {}
for _ in range(N):
    contact = input().split()
    name = contact[0]
    number = int(contact[1])
    book[number] = [0, name]

D = int(input())
for _ in range(D):
    number = int(input())
    book[number][0] += 1

book = sorted(book.items(), key = lambda x: x[0])
book.sort(key = lambda x: x[1][0], reverse=True)
print(book[0][1][1])