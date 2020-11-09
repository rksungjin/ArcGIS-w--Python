# Count characters

fIn = open("info.txt")

text = fIn.read()

outString = "The file contains %d characters" % (len(text))
print(outString)

fIn.close()

fIn = open("info.txt")

count = 0
for line in fIn :
    count = count + len(line)
    print(len(line))

outString = "The file contains %d characters" % (count)
print(outString)

fIn.close()
