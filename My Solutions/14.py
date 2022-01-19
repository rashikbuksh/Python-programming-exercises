s = input()
dictionary = {"UPPER": 0, "LOWER": 0}
for c in s:
    if c.isupper():
        dictionary["UPPER"] += 1
    elif c.islower():
        dictionary["LOWER"] += 1
    else:
        pass
print("UPPER CASE", dictionary["UPPER"])
print("LOWER CASE", dictionary["LOWER"])
