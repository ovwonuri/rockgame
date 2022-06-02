""" [Rock-Paper-Scissors]
Rock-Paper-Scissors is a simple two-player game where, at a
signal, players make figures with their hands, representing a
rock, a piece of paper, or a pair of scissors. The winner is determined according to a set of rules.
"""
# "R" for "rock",
# "P" for "paper",
# "S" for "scissors"
# Rock beats Scissors, Scissors beats Paper, Paper beats Rock

import random

# a list to hold the available choices in the game
available_choices = ['R', 'P', 'S']
selected_option = {"R": "ROCK", "P": "PAPER", "S": "SCISSORS"}


def search(original_list, u_choice):
    for i in range(len(original_list)):
        if original_list[i] == u_choice:
            return True
    return False


while True:
    # getting user choice between "R", "P" or "S"
    user_choice = input("please enter 'R' or 'P' or 'S': ").upper()

    if search(available_choices, user_choice):
        cpu_choice = random.choice(available_choices)
        print(f"player({selected_option[user_choice]}) : cpu({selected_option[cpu_choice]})")

        # There are six possibilities

        # possibilities of user winning
        # if user enters Rock and CPU enters Scissor = Rock wins
        if user_choice == available_choices[0] and cpu_choice == available_choices[2]:
            print("Player wins!!! congratulations!!!")
            break
        # if user enters Scissor and CPU enters Paper = Scissor wins
        elif user_choice == available_choices[2] and cpu_choice == available_choices[1]:
            print("Player wins!!! congratulations!!!")
            break
        # if user enters Paper and CPU enters Rock = Paper wins
        elif user_choice == available_choices[1] and cpu_choice == available_choices[0]:
            print("Player wins!!! congratulations!!!")
            break

        # possibilities of cpu winning
        # if CPU enters Rock and User enters Scissor = Rock wins
        elif cpu_choice == available_choices[0] and user_choice == available_choices[2]:
            print("CPU wins!!! congratulations!!!")
            break
        # if CPU enters Scissor and user enters Paper = Scissor wins
        elif cpu_choice == available_choices[2] and user_choice == available_choices[1]:
            print("CPU wins!!! congratulations!!!")
            break
        # if CPU enters Paper and CPU enters Rock = Paper wins
        elif cpu_choice == available_choices[1] and user_choice == available_choices[0]:
            print("CPU wins!!! congratulations!!!")
            break
        else:
            print("oh dear! This is a draw. try again or enter q to quit")
            continue
    else:
        print("user choice not found. Try again or enter q to quit")
        continue
