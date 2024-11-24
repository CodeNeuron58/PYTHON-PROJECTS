#choose the number of time a dice rolls , and outcome based on that. 

import random

while True:
    choice = input("ROLL THE DICE (Y/N): ").lower()
    if choice == "y":
        try:
            no_count=int(input("how many dice you want to roll: "))
            if no_count <=0:
                print("enter a posative number ")
                continue

            roll = [random.randint(1,6) for _ in range(no_count)]
            print(f"dice rolls : {', '.join(map(str,roll))}")

        except ValueError:
            print("invalid input !. please enter a valid number")

    elif choice == "N":
        print("Thanks for playing!")
        break

    else:
        print("Invalid input. Please enter 'Y' or 'N'.")        





