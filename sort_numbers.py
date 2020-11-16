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

print("Numbers:")
print(numbers)
print("Maximum:")
print(max(numbers))
print("Minimum:")
print(min(numbers))
numbers.sort()
print("Sorted:")
print(numbers)