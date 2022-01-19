def putNumbers(n):
    for i in range(0, n + 1):
        j = i
        i = i + 1
        if j % 7 == 0:
            yield j


n = int(input())
for i in putNumbers(n):
    print(i)
