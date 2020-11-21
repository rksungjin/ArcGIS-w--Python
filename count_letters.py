# Count the letters in a file

fIn = open("thesonnets.txt")

letterCounts = dict()

for line in fIn:
    letters = list(line)
    for letter in letters:
        letterCounts[letter] = letterCounts.get(letter, 0) + 1

print(letterCounts)