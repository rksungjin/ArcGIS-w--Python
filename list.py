# List the words in a text file in alpha order

fIn = open("shorttext.txt")

wordList = list()

for line in fIn:
    words = line.split()
    for word in words:
        if word not in wordList:
            wordList.append(word)