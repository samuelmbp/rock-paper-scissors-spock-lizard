"""
First steps: 

1. Get input from the user
2. Randomly choose an action for the computer
3. Display the two choices

Play it again:

4. Give the user the choice as to weather they want to play again
5. Embed the logic in a loop
6. Add another call to input() to get their choice

Determine the winner:

7. Rock smashes scissors
8. Paper covers rock
9. Scissors cut paper

"""
import random

CHOICES = ["rock", "paper", "scissors"]

BEATS = {
    "rock": ["scissors"],
    "paper": ["rock"],
    "scissors": ["paper"],
}

MESSAGES = {
    ("rock", "scissors"): "smashes",
    ("paper", "rock"): "covers",
    ("scissors", "paper"): "cut",
}


def show_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print(f"It's a tie! Both users chose '{user_choice}' ")
    elif user_choice not in BEATS.keys():
        print(f"\nYou typed '{user_choice}' which isn't a valid throw.")
    else:
        # BEATS[user_choice] is the list of things user_choice wins over
        user_wins = computer_choice in BEATS[user_choice]

        if user_wins:
            verb = MESSAGES[(user_choice, computer_choice)]
            print(
                f"{user_choice.capitalize()} {verb} {computer_choice}, you win!"
            )
        else:
            verb = MESSAGES[(computer_choice, user_choice)]
            print(
                f"{computer_choice.capitalize()} {verb} {user_choice}, you lose!"
            )

while True:
    print("Make a throw")
    user_choice = input("   Type: rock, paper or scissors: ")
    computer_choice = random.choice(CHOICES)
    print(
        f"\nYou threw '{user_choice}', the computer threw '{computer_choice}'")
    show_winner(user_choice, computer_choice)

    play_again = input('\nPlay again? (y/n): ')

    if (play_again.lower() != 'y'):
        break

print("\nGoodbye!")
