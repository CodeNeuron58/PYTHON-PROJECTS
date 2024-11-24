import random

def play_game():
    num_to_guess = random.randint(1, 100)
    attempts = 0  # Track the number of attempts
    max_attempts = 10  # Maximum number of attempts allowed

    print("Welcome to the Number Guessing Game! Guess a number between 1 and 100.")

    while attempts < max_attempts:
        try:
            user_guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - ENTER YOUR NUMBER: "))
            
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
                break  # Exit the loop since the user has won

            # Give feedback about remaining attempts
            if attempts < max_attempts:
                print(f"You have {max_attempts - attempts} attempts left.")

        except ValueError:
            print("Invalid input! Please enter a valid number between 1 and 100.")

    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {num_to_guess}.")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        play_game()  # Restart the game if the user says 'yes'
    else:
        print("Thanks for playing! Goodbye!")

# Start the game
play_game()
