#Calculate pay

def calculatePay (r, h) : 
    if h <= 40 :
        p = r * h

    else: 
        p = r * 40 + (h -40) * 1.5 * r
        return p

fOut = open("payroll.csv", "w")
    
while True:
    name = input("Enter Name: ")
    if name == 'done':
        break
    try: 
        hoursString = input("Enter hours: ")
        hours = float(hoursString)
    except: 
        print("Error, please enter numberic input") 
        continue
    try:     
        rateString = input("Enter rate: ")
        rate = float(rateString)
    except: 
        print("Error, please enter numberic input") 
        continue

    pay = calculatePay(rate, hours)
    outString = "%s, %.1f,%.2f,%.2f\n" % (name, hours, rate, pay)
    fOut.write(outString)
    print(outString)
#2 decimal places of accuracy
#spaces/ field width then decimal place below
    print("Gross pay: %.2f" % (pay))