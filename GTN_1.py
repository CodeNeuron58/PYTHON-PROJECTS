import random

num_to_guess = random.randint(1, 100)
attempts = 0  # Track the number of attempts

print("Welcome to the Number Guessing Game! Guess a number between 1 and 100.")

while True:
    try:
        user_guess = int(input("ENTER YOUR NUMBER: "))
        
        if user_guess < 1 or user_guess > 100:
            print("Please enter a valid number between 1 and 100.")
            continue  # Skip the rest of the loop and prompt again
        
        attempts += 1  # Increment the attempts count
        
        if user_guess > num_to_guess:
            print("Your guess is too high!")
        elif user_guess < num_to_guess:
            print("Your guess is too low!")
        else:
            print(f"BOOYAH! You guessed it correctly in {attempts} attempts.")
            print(f"THE NUMBER WAS {num_to_guess}.")
            break 
         # Exit the loop since the user has won
        
    except ValueError:
        print("Invalid input! Please enter a valid number between 1 and 100.")

    