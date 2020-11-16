# Get list of numbers and sort them

numbers = list() # or []

while True:
    valueString = input("Enter a number, 'done' to stop: ")
    if valueString == 'done':
        break
    try:
        value = int(valueString)
    except:
        print("Enter an integer!")
        continue
    numbers.append(value)

print("Numbers:", numbers)
#print(numbers)
print("Maximum:", max(numbers))
#print(max(numbers))
print("Minimum:", min(numbers))
#print(min(numbers))
print("Total:", sum(numbers))
print("Count:", len(numbers))
numbers.sort()
print("Sorted:", numbers)
#print(numbers)