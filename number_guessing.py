import random

secret_number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10")

while True:
    guess = input("Take a guess: ")
    
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {secret_number} correctly!")
        break