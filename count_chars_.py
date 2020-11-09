# Count characters

fIn = open("info.txt")

text = fIn.read()

outString = "The file contains %d characters" % (len(text))