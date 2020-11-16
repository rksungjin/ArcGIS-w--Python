# List the words in a text file in alpha order

fIn = open("shorttext.txt")

wordList = list()

for line in fIn:
    #print(line)
    words = line.split()
    #print(words)
    for word in words:
        if word.lower() not in wordList:
            wordList.append(word.lower())

#print(wordList)
wordList.sort()

print(wordList)