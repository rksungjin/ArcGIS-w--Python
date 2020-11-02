#Guessing Game

target = 42
guesses = 7

while guesses > 0:
    guessString = input("Guess my number: ")
    try: 
        guess = int(guessString)
    except: 
        print("Enter a number!")
        exit()
        continue
    guesses = guesses - 1
    if guess < target: 
        print("Higher!")
    if guess > target:
        print("Lower!")
    else: 
        print("You Win!")
        break