#Calculate pay

def calculatePay (r, h) : 
    if h <= 40 :
        p = r * h

    else: 
        p = r * 40 + (h -40) * 1.5 * r
        return p

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

pay = calculatePay(rate, hours)
print("Gross pay: ", pay)