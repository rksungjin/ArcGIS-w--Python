#Calculate pay

def calculatePay (r, h) : 
    if h <= 40 :
        p = r * h

    else: 
        p = r * 40 + (h -40) * 1.5 * r