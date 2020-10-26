# Calculate pay
hoursString = input("Enter hours: ")
hours = float(hoursString)

rateString = input("Enter rate: ")
rate = float(rateString)

if hours <= 40: 
    pay = hours * rate
else:
    pay = 40 * rate + (hours - 40) * 1.5 * rate

print("Pay: ", pay)