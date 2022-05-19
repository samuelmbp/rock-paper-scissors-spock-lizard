"""
First steps: 

1. Get input from the user
2. Randomly choose an action for the computer
3. Display the two choices
"""
import random

user_choice = input("Enter your choice: ")
computer_choice = random.choice(["rock", "scissors", "rock"])

print(f"User choice: {user_choice}")
print(f"Computer choice: {computer_choice}")