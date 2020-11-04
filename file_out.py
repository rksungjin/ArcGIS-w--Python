fileOut = open("contacts.csv", "w")
fileOut.write("Name, Age, PhoneNumber\n")
while True:
    name = input("Enter name: ")
    if name == "done":
        break
    age = -1
    while age < 0:
        try:
            ageString = input("Enter age: ")
            age = int(ageString)
        except:
            print("Invalid age!")
            continue
    phone = input("Enter phone number: ")