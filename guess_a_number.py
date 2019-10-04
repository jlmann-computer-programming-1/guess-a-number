import random

rand = random.randint(1, 100)
print("I'm thinking of a number from 1 to 100.")
print("")

guess = 0

while guess != rand:
    user_guess = input("Take a guess: \n")
    
    try:
        guess = int(user_guess)
    
        if guess < rand:
            print("You guessed too low.")
            
        elif guess > rand:
            print("You guessed too high.")

    except:
        print("Please type a number!")

print("")
print("You got it!")
print("Game over")
