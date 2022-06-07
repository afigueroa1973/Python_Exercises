# Exercise 2.15 (Sort in Ascending Order):

""" After a running competition, three runners want to determine who won based
    on the time they needed to complete the course. Write a script that inputs
    the time they took through three different floating-point numbers (in
    seconds) from the user. Display the numbers in increasing order. Prove that
    your script works by running it on all six possible orderings of the
    numbers. Does your script work with duplicate numbers?"""

player1 = int(input("\nEnter the time in seconds for Player 1: "))
player2 = int(input("Enter the time in seconds for Player 2: "))
player3 = int(input("Enter the time in seconds for Player 3: "))

if player1 < player2 < player3:
    print(f"""
    1st place: {player1} seconds for Player 1
    2nd place: {player2} seconds for Player 2
    3rd place: {player3} seconds for Player 3""")

if player1 < player3 < player2:
    print(f"""
    1st place: {player1} seconds for Player 1
    2nd place: {player3} seconds for Player 3
    3rd place: {player2} seconds for Player 2""")

if player2 < player1 < player3:
    print(f"""
    1st place: {player2} seconds for Player 2
    2nd place: {player1} seconds for Player 1
    3rd place: {player3} seconds for Player 3""")

if player2 < player3 < player1:
    print(f"""
    1st place: {player2} seconds for Player 2
    2nd place: {player3} seconds for Player 3
    3rd place: {player1} seconds for Player 1""")

if player3 < player1 < player2:
    print(f"""
    1st place: {player3} seconds for Player 3
    2nd place: {player1} seconds for Player 1
    3rd place: {player2} seconds for Player 2""")

if player3 < player2 < player1:
    print(f"""
    1st place: {player3} seconds for Player 3
    2nd place: {player2} seconds for Player 2
    3rd place: {player1} seconds for Player 1""")

# Does your script work with duplicate numbers? No, it doesn't work
