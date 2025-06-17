import random

print("Welcome to the Number Guessing Game!")
number = random.randint(1, 100)

while True:
    guess = input("Guess a number between 1 and 100: ")
    
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it right.")
        break
