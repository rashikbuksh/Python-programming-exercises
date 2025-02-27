from operator import itemgetter

freq = {}
line = input()
for word in line.split():
    freq[word] = freq.get(word, 0) + 1

words = freq.keys()
sorted(words, key=itemgetter(0))

for w in words:
    print("%s:%d" % (w, freq[w]))
