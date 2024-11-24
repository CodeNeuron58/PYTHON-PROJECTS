#choose the number of time a dice rolls , and outcome based on that. 

import random
import time  # Import time module to add delays

# Initialize roll counter
roll_count = 0

while True:
    # Ask if the user wants to roll the dice or quit
    choice = input("ROLL THE DICE (Y/N) or Q to quit: ").strip().lower()
    #strip() remove extra spaces
    if choice == "y":
        roll_count += 1  # Increment the roll counter
        try:
            # Ask for the number of dice to roll
            no_count = int(input("How many dice do you want to roll? "))
            if no_count <= 0:
                print("Please enter a positive number of dice.")
                continue  # Restart the loop if input is invalid
            
            # Simulate dice rolling with a message
            print("WAIT! The dice are rolling... Please wait.")
            time.sleep(3)  # Wait for 3 seconds to simulate rolling
            
            # Generate dice rolls and calculate the sum
            roll = [random.randint(1, 6) for _ in range(no_count)]
            dice_sum = sum(roll)
            
            # Display the results
            print(f"Dice rolls: {', '.join(map(str, roll))}")
            print(f"Sum of the rolls: {dice_sum}")
            print(f"You have rolled the dice {roll_count} times.")
        
        except ValueError:
            print("Invalid input! Please enter a valid number for the dice count.")
    
    elif choice == "n":
        print("Thanks for playing!")
        break  # Exit the loop if user chooses to stop

    elif choice == "q":
        print("You chose to quit. Thanks for playing!")
        break  # Exit the loop if user types 'Q' to quit
    
    else:
        print("Invalid input. Please enter 'Y' to roll, 'N' to quit, or 'Q' to quit early.")

