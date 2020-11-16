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

for i in range(len(wordList)):
    smallest = i
    #smallest = wordList[i].lower()
    for j in range(len(wordList) - i):
        if wordList[i+j].lower() < wordList[smallest].lower():
            smallest = i+j
        temp = wordList[i+j]
        wordList[i+j] = wordList[i]
        wordList[i] = temp
        
print(wordList)