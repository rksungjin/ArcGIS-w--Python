#Calculate pay

def calculatePay (r, h) : 
    if h <= 40 :
        p = r * h

    else: 
        p = r * 40 + (h -40) * 1.5 * r
        return p

def getHours():
    hoursString = input("Enter hours: ")
    h = -1
    try: 
        h = float(hoursString)
    except: 
        print("Error, please enter numeric input for hours")
    return h
    
def getRate():
    rateString = input("Enter rate: ")
    r = -1
    try: 
        r = float(rateString)
    except: 
        print("Error, please enter numeric input for rate")
    return r

fOut = open("payroll.csv", "w")
    
while True:
    name = input("Enter Name: ")
    if name == 'done':
        break
    hours = -1
    while hours < 0: 
        hours = getHours
    rate = -1
    while rate < 0:
        rate = getRate()
    #try: 
        #hoursString = input("Enter hours: ")
        #hours = float(hoursString)
    #except: 
        #print("Error, please enter numberic input") 
        #continue
    #try:     
        #rateString = input("Enter rate: ")
        #rate = float(rateString)
    #except: 
        #print("Error, please enter numberic input") 
        #continue

    pay = calculatePay(rate, hours)
    outString = "%s, %.1f,%.2f,%.2f\n" % (name, hours, rate, pay)
    fOut.write(outString)
    print(outString)
fOut.close()
#2 decimal places of accuracy
#spaces/ field width then decimal place below
    #print("Gross pay: %.2f" % (pay))