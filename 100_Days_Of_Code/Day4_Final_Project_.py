# Day 4 Final Project, Rock, Paper or Scissor:

""" Write a program for the Rock, Paper or Scissor game. From there you will
    need to figure out:
    - How you will store the user's input.
    - How you will generate a random choice for the computer.
    - How you will compare the user's and the computer's choice to determine
    the winner (or a draw).
    - And also how you will give feedback to the player."""

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

user_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper "
                        "or 2 for Scissor: "))

if user_choice == 0:
    print("You chose: Rock")
elif user_choice == 1:
    print("You chose: Paper")
elif user_choice == 2:
    print("You chose: Scissor")

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, try again!")
else:
    print(images[user_choice])

    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print("Computer chose: Rock")
    elif computer_choice == 1:
        print("Computer chose: Paper")
    elif computer_choice == 2:
        print("Computer chose: Scissor")

    print(images[computer_choice])

    if user_choice == 0 and computer_choice == 0:
        print("It was a draw!")
    elif user_choice == 0 and computer_choice == 1:
        print("Sorry, you lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("Congratulations, you win!")

    elif user_choice == 1 and computer_choice == 0:
        print("Congratulations, you win!")
    elif user_choice == 1 and computer_choice == 1:
        print("It was a draw!")
    elif user_choice == 1 and computer_choice == 2:
        print("Sorry, you lose!")

    elif user_choice == 2 and computer_choice == 0:
        print("Sorry, you lose!")
    elif user_choice == 2 and computer_choice == 1:
        print("Congratulations, you win!")
    elif user_choice == 2 and computer_choice == 2:
        print("It was a draw!")
