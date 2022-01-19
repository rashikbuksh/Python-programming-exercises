values = input()
numbers=[]
for x in values.split(","):
    if int(x) % 2 != 0:
        numbers.append(x)
print(",".join(numbers))
