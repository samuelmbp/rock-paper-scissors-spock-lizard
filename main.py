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
from choice import Choice

CHOICES = [f"{choice.name} [{choice.value}]" for choice in Choice]
CHOICES_STR = ", ".join(CHOICES)

BEATS = {
    Choice.Rock: [Choice.Lizard, Choice.Scissors],
    Choice.Paper: [Choice.Spock, Choice.Rock],
    Choice.Scissors: [Choice.Lizard, Choice.Paper],
    Choice.Lizard: [Choice.Spock, Choice.Paper],
    Choice.Spock: [Choice.Scissors, Choice.Rock],
}

MESSAGES = {
    (Choice.Rock, Choice.Scissors): "crushes",
    (Choice.Rock, Choice.Lizard): "crushes",
    (Choice.Paper, Choice.Rock): "covers",
    (Choice.Paper, Choice.Spock): "disproves",
    (Choice.Scissors, Choice.Paper): "cut",
    (Choice.Scissors, Choice.Lizard): "decapitates",
    (Choice.Lizard, Choice.Paper): "eats",
    (Choice.Lizard, Choice.Spock): "poisons",
    (Choice.Spock, Choice.Scissors): "smashes",
    (Choice.Spock, Choice.Rock): "vaporize",
}


def show_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print(f"It's a tie! Both users chose '{user_choice.name}'")
    else:
        # BEATS[user_choice] is the list of things user_choice wins over
        user_wins = computer_choice in BEATS[user_choice]

        if user_wins:
            verb = MESSAGES[(user_choice, computer_choice)]
            print(
                f"{user_choice.name} {verb} {computer_choice.name.lower()}, you win!"
            )
        else:
            verb = MESSAGES[(computer_choice, user_choice)]
            print(
                f"{computer_choice.name} {verb} {user_choice.name.lower()}, you lose!"
            )


while True:
    print("Make a throw")
    try:
        value = input(f"   Enter a choice: ({CHOICES_STR}):  ")
        user_choice = Choice(int(value))
    except:
        print(f"\nYou typed '{value}' which isn't a valid choice.")
        continue

    value = random.randint(0, len(Choice) - 1)
    computer_choice = Choice(value)
    show_winner(user_choice, computer_choice)

    play_again = input('\nPlay again? (y/n): ')

    if (play_again.lower() != 'y'):
        break

    print()

print("\nGoodbye!")
