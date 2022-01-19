def lenCheck(a, b):
    len1 = len(a)
    len2 = len(b)
    if len1 > len2:
        print(a)
    elif len2 > len1:
        print(b)
    else:
        print(a)
        print(b)


string1 = input()
string2 = input()
lenCheck(string1, string2)
