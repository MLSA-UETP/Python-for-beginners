import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Initialize a counter variable
guesses = 0

# Use a while loop to keep asking for guesses until the user guesses the correct number
while True:
    # Ask the user for a guess
    guess = input("Guess a number between 1 and 100: ")
    guess = int(guess)
    
    # Increment the counter
    guesses += 1
    
    # Check if the guess is correct
    if guess == number:
        print("Congratulations! You guessed the correct number in", guesses, "guesses.")
        break
    elif guess < number:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")
