#Reverse user input

text = input("Enter some text: ")

index = len(text) - 1
newText = ""

while index >= 0: 
    newText = newText + text[index]
    index = index - 1

print(newText)