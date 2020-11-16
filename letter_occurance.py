# Count occurances of letters

letterCount = dict()
text = 'extraordinary'
for c in text:
    if c not in letterCount:
        letterCount[c] = 1
    else:
        letterCount[c] = letterCount[c] + 1
    print(letterCount)
print(letterCount)