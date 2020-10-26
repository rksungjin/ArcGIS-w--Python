# Calculate pay
try: 
    hoursString = input("Enter hours: ")
    hours = float(hoursString)
except: 
    print("Error, please enter numberic input") 
    exit(0)
try:     
    rateString = input("Enter rate: ")
    rate = float(rateString)
except: 
    print("Error, please enter numberic input") 
    exit(0)

if hours <= 40: 
    pay = hours * rate
    print("Gross Pay: ", pay)
else:
    basepay = 40 * rate
    overtime = (hours - 40) * 1.5 * rate
    pay = basepay + overtime
    #pay = 40 * rate + (hours - 40) * 1.5 * rate
    print("Gross Pay: ", pay, "Base Pay: ", basepay, "Overtime Pay: ", overtime)
