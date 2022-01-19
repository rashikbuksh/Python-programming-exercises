from operator import itemgetter

list = []
while True:
    s = input()
    if not s:
        break
    list.append(tuple(s.split(",")))

print(sorted(list, key=itemgetter(0, 1, 2)))
