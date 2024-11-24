#general 

import random

while True:
    any_choice = input("ROLL THE DICE (Y/N): ").upper()
    
    if any_choice == "Y":
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        print(f"{die_1}, {die_2}")
    
    elif any_choice == "N":
        print("Thanks for playing")
        break

    else:
        print("Invalid input")
