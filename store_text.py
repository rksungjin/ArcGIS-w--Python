
fOut = open("info.txt", "w")

print("Enter some text, 'done' to stop:")

while True :
    text = input()
    if text == 'done':
        break
fOut.write(text + '\n')
fOut.close()

print("The new file contains:")

fIn = open("info.txt")

for line in fIn:
    print(line, end="")

fIn.close()
