# Day 3 Final Project, Choose Your Own Adventure:

""" Make your own "Choose Your Own Adventure" game. Use conditionals such as
    if, else, and elif statements to lay out the logic and the story's path in
    your program.

    Text Snippets from example:
    - You're at a crossroad. Where do you want to go? Type "left" or "right"
    - You've come to a lake. There is an island in the middle of the lake. Type
    "wait" to wait for a boat. Type "swim" to swim across.
    - You arrive at the island unharmed. There is a house with 3 doors. One red
    one yellow and one blue. Which colour do you choose?
    - It's a room full of fire. Game Over!
    - You found the treasure! You Win!
    - You enter a room of beasts. Game Over!
    - You chose a door that doesn't exist. Game Over!
    - You get attacked by an angry trout. Game Over!
    - You fell into a hole. Game Over!"""

print('''
        888
        888
        888
        8888888888888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.
        888   888P   d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b
        888   888    88888888.d888888"Y8888b.888  888888    88888888
        888b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.
         Y888888      Y8888 "Y888888 88888P'  Y88888888      Y8888

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

print("Welcome To Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a cross road. Where do you want to go?...Type '
                '"left" or "right"\n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle '
                    'of the lake. Type "wait" to wait for a boat. Type "swim" '
                    'to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house "
                        "with 3 doors. One red, one yellow and one blue. "
                        "Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over!")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over!")
        else:
            print("You chose a door that doesn't exist. Game Over!")
    else:
        print("You get attacked by an angry trout. Game Over!")
else:
    print("You fell into a hole...Game Over!")
