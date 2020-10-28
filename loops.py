#Infinite loop

while True:
    text = input(">")
    if text == "done":
        break
    print(text)

print("Finished!")

#For loop
values = [17,6,8,23,1,4,7,11,30,12]
smallest = values[0]
largest = values[0]
for x in values:
    if smallest > x:
        smallest = x
    if largest < x:
        largest = x
    print("x = ", x, "smallest = ", smallest, "largest =", largest)
print(smallest)
print(largest)