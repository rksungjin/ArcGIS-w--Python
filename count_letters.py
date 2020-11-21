# Count the letters in a file

fIn = open("thesonnets.txt")
text = fIn.read()
fIn.close()

letterCounts = dict()

vowels = ['a', 'e', 'i', 'o', 'u']

letters = list(text.lower())
#for line in fIn:
    #letters = list(line)
for letter in letters:
    if letter in vowels:
        letterCounts[letter] = letterCounts.get(letter, 0) + 1
counts = list()

for k,v in letterCounts.items():
    counts.append((v,k))
counts.sort()

print(counts)