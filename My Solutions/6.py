import math

C = 50
H = 30
value = []
items = [x for x in input().split(',')]
for i in items:
    value.append(str(int(round(math.sqrt(2 * C * float(i) / H)))))

print(','.join(value))
