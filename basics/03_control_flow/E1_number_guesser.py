import random

max_number = 100

print("\nWelcome to my game!\n"
      "Now I will generate a random number from 0 to 100 and you have to guess it."
      "\nLet's start...\n")

while True:
    number_to_guess = random.randint(0, max_number)

    player_guess = int(input("Try to guess!\n "))

    if number_to_guess != player_guess:
        print(f"You lost! The right number was {number_to_guess}")
    else:
        print("Well done! You won!")

    choice = input("Do you want to continue? (y/N) ").capitalize()

    if choice in ["Y", "Yes"]:
        continue
    else:
        break