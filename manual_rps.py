""""""

import random

def get_computer_choice():
    """Function gets a random choice out of rock, paper, scissors for the computer"""
    choice_list = ["Rock","Paper","Scissors"]
    computer_choice = random.choice(choice_list)
    return computer_choice

def get_user_choice():
    """Gets users selection out of rock, paper scissors"""
    user_input =  input("Select an option from rock, paper, scissors")
    return user_input
