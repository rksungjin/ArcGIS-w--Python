# Convert grade to letter

def computeGrade(s):
    if s > 100 or s < 0:
        letterGrade = "Bad Score"
    elif s>= 90:
        letterGrade = "A"
    elif s>= 80:
        letterGrade = "B"
    elif s>= 70:
        letterGrade = "C"
    elif s>= 60:
        letterGrade = "D"
    else:
        letterGrade = "F"
    return letterGrade

try:
    scoreString = input("Enter score: ")
    score = int(scoreString)

except:
    print("Bad Score")
    exit(0)

letter = computeGrade(score)
print(letter)


#if score > 100 or score < 0: 
    #print ("Bad Score")
#elif score >= 90 : 
    #print ("A")
#elif score >=80 : 
    #print ("B")
#elif score >=70 : 
    #print ("C")
#elif score >=60 :
    #print ("D")
#else: 
    #print("F")