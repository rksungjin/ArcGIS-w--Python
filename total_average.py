#Count, total and average of user input

count = 0
total = 0
smallest = None
largest = None

while True: 
    valueString = input("Enter a number: ")
    if valueString == "done" :
        break
    try : 
        value = int(valueString)
    except : 
        print("Invalid input")
        continue
    count = count + 1
    total = total + value
    if smallest == None or smallest > value : 
        smallest = value
    if largest == None or largest < value :
        largest = value

print("Total: ", total)
print("Count: ", count)
print("Average: ", total/count)

if count == 0 :
    print("Average: 0")
else :
    print("Average: ", total/count)
print("Largest: ", largest)
print("Smallest: ", smallest)