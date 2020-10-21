#condition execution examples 
xString = input("Enter a number: ")
yString = input("Enter another number: ")

x = int(xString)
y = int(yString)

if x > y : 
    print(x, "is greater than", y)
elif x < y : 
    print (x, "is less than", y)
else : 
    print (x, "is equal to", y)