#Guessing Game

target = 42

guessString = input("Guess my number: ")
try: 
    guess = int(guessString)
except: 
    print("Enter a number!")
    exit()

if guess < target: 
    print("Higher!")
if guess > target:
    print("Lower!")
else: 
    print("You Win!")