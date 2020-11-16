f = open('shorttext.txt')
counts = dict()
for line in f:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

wordList = list(counts.keys())
wordList.sort()
for k in wordList:
    print(k, counts[k])

#print(counts)