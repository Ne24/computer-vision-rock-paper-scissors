""""""

import random

def get_computer_choice():
    """Function gets a random choice out of rock, paper, scissors for the computer"""
    choice_list = ["Rock","Paper","Scissors"]
    computer_choice = random.choice(choice_list)
    # computer_choice = computer_choice.lower()
    return computer_choice

def get_user_choice():
    """Gets users selection out of rock, paper scissors"""
    user_input =  input("Select an option from rock, paper, scissors ")
    user_input = user_input.title()
    return user_input

def get_winner(computer_choice, user_choice):
    """Determines the winner of the rock-paper-scissors game """
    if computer_choice == user_choice:
        print("It is a tie!")
    elif computer_choice == "Rock" and user_choice == "Scissors":
        print("You lost")
    elif computer_choice == "Paper" and user_choice == "Rock":
        print("You lost")
    elif computer_choice == "Scissors" and user_choice == "Paper":
        print("You lost")
    else:
        print("You won!")
    return

def play():
    """Play the rock-paper-scissors game"""

    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice,user_choice)

play()
