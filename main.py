"""
First steps: 

1. Get input from the user
2. Randomly choose an action for the computer
3. Display the two choices

Play it again:

4. Give the user the choice as to weather they want to play again
5. Embed the logic in a loop
6. Add another call to input() to get their choice
"""
import random

CHOICES = ["rock", "paper", "scissors"]

while True:
    print("Make a throw")
    user_choice = input("Type: rock, paper or scissors: ")

    if user_choice in CHOICES:
        computer_choice = random.choice(CHOICES)
        print(
            f"\nYou threw '{user_choice}', the computer threw '{computer_choice}'"
        )
    else:
        print(f"\nYou typed '{user_choice}' which isn't a valid throw.")

    play_again = input('\nPlay again? (y/n): ')

    if (play_again.lower() != 'y'):
        break

print("\nGoodbye!")
    




















