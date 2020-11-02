#Count, total and average of user input

count = 0
total = 0

while True: 
    valueString = input("Enter a number: ")
    if valueString == "done" :
        break
    try : 
        value = int(valueString)
    except : 
        print("Invalid input")